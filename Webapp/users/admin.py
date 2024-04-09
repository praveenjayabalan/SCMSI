from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User,Group


admin.site.register(Profile)
admin.site.unregister(User)
admin.site.unregister(Group)
