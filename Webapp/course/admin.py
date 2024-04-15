from django.contrib import admin
from .models import CourseMaster
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    model = CourseMaster
    fields = ['course_name','course_desc']
    list_display = ['course_name','course_desc']      


admin.site.register(CourseMaster, CourseAdmin)
