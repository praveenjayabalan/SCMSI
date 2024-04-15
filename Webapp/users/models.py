from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import datetime
from course.models import *

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    # added columns
    phone = models.TextField(null = True)
    address = models.TextField(null = True)
    twelth_percentage = models.IntegerField(null = True,max_length=10)
    consulting_date = models.DateField(default=datetime.datetime.now, blank=True)
    is_approved = models.BooleanField(default = False)
    tenth_marksheet = models.ImageField(default='default.jpg', upload_to='tenth_marksheet_images')
    twelth_marksheet = models.ImageField(default='default.jpg',upload_to='twelth_marksheet_images')
    course_id = models.IntegerField(default=0,null =True)
    # course = models.ForeignKey(CourseMaster,  null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)