from django.contrib import admin
from Mhealth.models import SmartPhoneMeta, Patient


@admin.register(SmartPhoneMeta)
class SmartPhoneMetaAdmin(admin.ModelAdmin):
    pass


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass
