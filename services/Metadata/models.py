from django.db import models


class Doctor(models.Model):
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    specialty = models.CharField(max_length=1000)


class Center(models.Model):
    location = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)


class Ambulance(models.Model):
    location = models.CharField(max_length=1000)
