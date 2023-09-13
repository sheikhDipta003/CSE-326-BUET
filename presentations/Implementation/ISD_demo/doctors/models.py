from django.db import models

# Create your models here.
class Doctor(models.Model):
    Doctor_ID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Password = models.CharField(max_length=50,null=True)
    Qualifications = models.CharField(max_length=100)
    Shift = models.CharField(max_length=50)

    def __str__(self):
        return self.Name