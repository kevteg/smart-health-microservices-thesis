from django.contrib import admin
from Medrecords.models import Record, Patient


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass
