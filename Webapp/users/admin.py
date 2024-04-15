from pydoc import resolve
from django.contrib import admin
from django.http import HttpRequest
from .models import Profile
from configdata.models import ConfigurationMaster
from django.contrib.auth.models import User,Group

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
    fields = ['is_approved','phone','address','bio','avatar','twelth_percentage']
    list_display = ['user','phone', 'address', 'twelth_percentage']     

    def get_queryset(self,request):        
        qs= super().get_queryset(request)        
        return qs.filter(twelth_percentage__gte = 60)

    def has_add_permission(self, request,obj = None):
        return False
   
           
    
# admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
    