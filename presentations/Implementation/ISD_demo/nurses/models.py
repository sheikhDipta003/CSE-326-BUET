from django.db import models
from doctors.models import Doctor
from residents.models import CheckupItem,MedCond

class Nurse(models.Model):
    Nurse_Id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50,null=True)
    Password = models.CharField(max_length=50,null=True)
    Qualifications = models.CharField(max_length=50)
    Shift = models.CharField(max_length=20)

    def __str__(self):
        return f"Checkup {self.Nurse_Id} Qualifications {self.Qualifications} Shift {self.Shift}"

class Member(models.Model):
    Member_ID = models.AutoField(primary_key=True)
    Room_no = models.IntegerField()
    Name = models.CharField(max_length=100)
    Password = models.CharField(max_length=50,null=True)
    Address = models.TextField()
    Email = models.EmailField()
    Phone = models.CharField(max_length=15)
    DOB = models.DateField()
    Religion = models.CharField(max_length=50)
    Account_no = models.CharField(max_length=20)
    Assigned_nurse=models.ForeignKey(Nurse, on_delete=models.CASCADE)
    riskrate=models.IntegerField(default=0)
    Assigned_doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f"{self.Name} {self.Member_ID}"

class MemberNurse(models.Model):
    Room_no = models.ForeignKey(Member, on_delete=models.CASCADE)
    Nurse_ID = models.ForeignKey(Nurse, on_delete=models.CASCADE)

    # Define the primary key constraint for the combination of Room_no and Nurse_ID
    class Meta:
        unique_together = ('Room_no', 'Nurse_ID')

    def __str__(self):
        return f"MemberNurse - Room {self.Room_no.Room_no}, Nurse {self.Nurse_ID.Name}"

class CheckupSchedule(models.Model):
    Checkup_Id=models.OneToOneField(CheckupItem, primary_key=True, on_delete=models.CASCADE)
    Member_Id = models.ForeignKey(Member, on_delete=models.CASCADE)
    Nurse_Id = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    Doctor_ID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Date = models.DateField()
    Completed = models.BooleanField(default=False)
    Exact_time=models.TimeField(default='09:00:00')
    Risk_rate=models.IntegerField(default=0)

    def __str__(self):
        return f"Checkup Schedule for {self.Checkup_Id}"

class SpecialCheckupSchedule(models.Model):
    Special_Checkup_Id = models.OneToOneField(CheckupItem, primary_key=True, on_delete=models.CASCADE)
    Member_Id = models.ForeignKey(Member, on_delete=models.CASCADE)
    Nurse_Id = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    Doctor_ID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Date = models.DateField()
    Frequency = models.PositiveIntegerField()
    Completed = models.BooleanField(default=False)
    Exact_time=models.TimeField(default='09:00:00')
    Risk_rate=models.IntegerField(default=0)

    def __str__(self):
        return f"Special Checkup Schedule for {self.Special_Checkup_Id}"

class ResidentMedCond(models.Model):
    Member_ID = models.ForeignKey(Member, on_delete=models.CASCADE)
    Cond_ID = models.ForeignKey(MedCond, on_delete=models.CASCADE)

class MemberAppoint(models.Model):
    App_ID = models.AutoField(primary_key=True)
    Member_ID = models.ForeignKey(Member, on_delete=models.CASCADE)
    Doctor_ID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Nurse_ID = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    Date = models.DateField()
    Time = models.TimeField()
    
class Medicine(models.Model):
    Medicine_id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=20)
    Mg=models.IntegerField()
    Company=models.CharField(max_length=50)
    Available=models.IntegerField()

    def __str__(self):
        return f"Medicine {self.Medicine_id} {self.Name}"
    
class MedicineChart(models.Model):
    Chart_id=models.AutoField(primary_key=True)
    Member_ID=models.ForeignKey(Member, on_delete=models.CASCADE)
    Date=models.DateField()
    
    def __str__(self):
        return f"Medicine chart {self.Chart_id} for {self.Member_id}"
    
class Dosage(models.Model):
    Medicine_id=models.ForeignKey(Medicine, on_delete=models.CASCADE)
    Chart_id=models.ForeignKey(MedicineChart, on_delete=models.CASCADE)
    # Time=models.CharField(max_length=50)
    Quantity=models.CharField(max_length=20)
    Exact_time=models.TimeField(default='09:00:00')

class CurrentCond(models.Model):
    Member_id=models.ForeignKey(Member, on_delete=models.CASCADE)
    Risk_rate=models.IntegerField()
    def __str__(self):
        return f"{self.Member_id} {self.Risk_rate}"

class SpecialCheckupScheduletwo(models.Model):
    Special_Checkup_Id = models.AutoField(primary_key=True)
    Member_Id = models.ForeignKey(Member, on_delete=models.CASCADE)
    Nurse_Id = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    Doctor_ID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Date = models.DateField()
    Frequency = models.PositiveIntegerField()
    Completed = models.BooleanField(default=False)
    Exact_time=models.TimeField(default='09:00:00')
    Risk_rate=models.IntegerField(default=0)

    def __str__(self):
        return f"Special Checkup Schedule for {self.Special_Checkup_Id}"
class SpecialCheckupItem(models.Model):
    Special_Checkup_Item_Id = models.AutoField(primary_key=True)
    Schedule_Id=models.ForeignKey(SpecialCheckupScheduletwo, on_delete=models.CASCADE)
    Blood_Pressure = models.CharField(max_length=20)
    Sugar = models.DecimalField(max_digits=5, decimal_places=2)
    Heartrate = models.IntegerField()
    
    def __str__(self):
        return f"Special Checkup {self.Special_Checkup_Id}"



