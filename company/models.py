from django.db import models

from utils.enumerators import Availability


class Company (models.Model):
    id = models.CharField(max_length=36, blank=False, primary_key=True)
    companyName = models.CharField(max_length=100, blank=False)
    observation = models.CharField(max_length=200, blank=True)
    availability = models.CharField(max_length=1, blank=False, choices=Availability.choices,
                                    default=Availability.AVAILABLE)
