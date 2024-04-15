from django.db import models

class CourseMaster(models.Model):
  course_name = models.CharField(max_length=100)
  course_desc = models.CharField(max_length=255)