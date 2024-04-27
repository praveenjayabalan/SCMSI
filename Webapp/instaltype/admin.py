from django.contrib import admin
from .models import InstallTypeMaster
# Register your models here.


class InstallTypeAdmin(admin.ModelAdmin):
    model = InstallTypeMaster
    fields = ['installment_period','installment_amt','installment_desc']
    list_display = ['installment_period','installment_amt','installment_desc']      


admin.site.register(InstallTypeMaster, InstallTypeAdmin)
