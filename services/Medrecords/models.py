from django.db import models
from django.contrib.postgres.fields import JSONField


class Patient(models.Model):
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    birth_date = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    notes = JSONField(null=True, blank=True)


class Record(models.Model):
    reason = models.CharField(max_length=1000)
    problems_summary = JSONField()
    diagnostic = models.CharField(max_length=1000)
    initial_planning = models.CharField(max_length=1000)
    consult_notes = JSONField(null=True, blank=True)
    medical_recomendations = JSONField(null=True, blank=True)
    summary = JSONField(null=True, blank=True)
    family_background = JSONField(null=True, blank=True)
    toxic_habits = JSONField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
