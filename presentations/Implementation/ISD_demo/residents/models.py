from django.db import models
# from nurses.models import SpecialCheckupSchedule
class MedCond(models.Model):
    Cond_ID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    Advice=models.CharField(max_length=150)
    Guideline=models.CharField(max_length=150)
    
class CheckupItem(models.Model):
    Checkup_Id = models.AutoField(primary_key=True)
    Blood_Pressure = models.CharField(max_length=20)
    Sugar = models.DecimalField(max_digits=5, decimal_places=2)
    Heartrate = models.IntegerField()

    def __str__(self):
        return f"Checkup {self.Checkup_Id}"
