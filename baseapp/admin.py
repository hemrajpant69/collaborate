from django.contrib import admin
from .models import Donor,Patient,Doctor

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Donor)
admin.site.register(Patient)
