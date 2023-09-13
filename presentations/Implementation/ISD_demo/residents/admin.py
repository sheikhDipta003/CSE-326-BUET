from django.contrib import admin

# Register your models here.
from .models import MedCond,CheckupItem

admin.site.register(MedCond)
admin.site.register(CheckupItem)