from pydoc import resolve
from django.contrib import admin
from django.http import HttpRequest
from django.http.response import HttpResponse
from .models import Profile
from configdata.models import ConfigurationMaster
from django.contrib.auth.models import User,Group
from django.core.mail import send_mail
from django.conf import settings

admin.site.unregister(User)
admin.site.unregister(Group)


class UserProfileInline(admin.StackedInline):      
    model = Profile
    fields = ['is_approved','phone','address','bio','avatar','twelth_percentage']
    list_filter = ['is_approved']


class UserAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline]
    fields = ['username','first_name','last_name','email','is_active']
    list_display = ['username', 'email', 'first_name', 'last_name','is_active']     
            
    def get_queryset(self,request):        
        qs= super().get_queryset(request)        
        return qs.filter(is_staff = False)
    
    def has_add_permission(self, request,obj = None):
        return False
    
    
class ProfileAdmin(admin.ModelAdmin):    
    fields = ['is_approved','phone','address','bio','avatar','twelth_percentage','consulting_date','tenth_marksheet','twelth_marksheet','installation_type','is_fee_paid']
    list_display = ['user','phone', 'address', 'twelth_percentage']     

    def get_queryset(self,request):        
        qs= super().get_queryset(request)      
        conf_per = int(ConfigurationMaster.objects.filter(config_name = "Percentage_limit").values_list('config_value',flat=True)[0]) 
        return qs.filter(twelth_percentage__gte = conf_per)

    def has_add_permission(self, request,obj = None):
        return False
    
    def response_change(self, request: HttpRequest, obj: None) -> HttpResponse:
        if obj.is_approved:
            # send email for approval
            subject = 'SCMS Application was approved'
            # get username and email
            userinfo = User.objects.get(id=obj.user_id)
            username =userinfo.username
            email =userinfo.email
            counslingdate = obj.consulting_date
                    
            message = f'Hi {username}, thanks for registering your counseling date has been scheduled on {counslingdate} '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail( subject, message, email_from, recipient_list )



        return super().response_change(request, obj)
    
   
           
    
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
    