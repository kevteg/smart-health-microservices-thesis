from django.contrib import admin
from Metadata.models import Doctor, Center, Ambulance


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass


@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    pass



@admin.register(Ambulance)
class AmbulanceAdmin(admin.ModelAdmin):
    pass
