from django.db import models

class CourseMaster(models.Model):
  course_name = models.CharField(max_length=100)
  course_desc = models.CharField(max_length=255)

  def __str__(self):
      return self.course_desc+' ('+self.course_name+')'