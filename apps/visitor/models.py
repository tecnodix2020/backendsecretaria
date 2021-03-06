from django.db import models

from utils.enumerators import Availability


class Visitor (models.Model):
    id = models.CharField(max_length=36, blank=False, primary_key=True)
    personalCode = models.CharField(max_length=36, blank=False, unique=True)
    idCompany = models.CharField(max_length=36, blank=True)
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False, unique=True)
    observation = models.CharField(max_length=200, blank=True)
    availability = models.CharField(max_length=1, blank=False, choices=Availability.choices,
                                    default=Availability.AVAILABLE.value)
