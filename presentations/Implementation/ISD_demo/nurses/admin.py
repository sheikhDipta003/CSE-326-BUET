from django.contrib import admin

# Register your models here.
from .models import Nurse, Member, MemberNurse, CheckupSchedule, SpecialCheckupSchedule, ResidentMedCond, MemberAppoint, Medicine, MedicineChart, Dosage, CurrentCond,SpecialCheckupScheduletwo,SpecialCheckupItem

admin.site.register(Nurse)
admin.site.register(Member)
admin.site.register(MemberNurse)
admin.site.register(CheckupSchedule)
admin.site.register(SpecialCheckupSchedule)
admin.site.register(ResidentMedCond)
admin.site.register(MemberAppoint)
admin.site.register(Medicine)
admin.site.register(MedicineChart)
admin.site.register(Dosage)
admin.site.register(CurrentCond)
admin.site.register(SpecialCheckupScheduletwo)
admin.site.register(SpecialCheckupItem)