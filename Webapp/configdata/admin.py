from django.contrib import admin
from .models import ConfigurationMaster
# Register your models here.


class ConfigAdmin(admin.ModelAdmin):
    model = ConfigurationMaster
    fields = ['config_name','config_value']
    list_display = ['config_name','config_value']  
    readonly_fields=['config_name']

    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(ConfigurationMaster, ConfigAdmin)
