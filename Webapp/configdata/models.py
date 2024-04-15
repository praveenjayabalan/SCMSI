from django.db import models

class ConfigurationMaster(models.Model):
  config_name = models.CharField(max_length=255)
  config_value = models.CharField(max_length=255)