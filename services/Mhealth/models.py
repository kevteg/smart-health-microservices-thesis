from django.db import models
from django.contrib.postgres.fields import JSONField


class Patient(models.Model):
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    birth_date = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


class SmartPhoneMeta(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=1000)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
