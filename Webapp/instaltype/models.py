from django.db import models

class InstallTypeMaster(models.Model):
  installment_period = models.CharField(max_length=100)
  installment_amt = models.IntegerField(default=0)
  installment_desc = models.CharField(max_length=255)

  def __str__(self):
      return self.installment_period

