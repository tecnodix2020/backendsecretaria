from django.db import models

from utils.enumerators import Availability


class Employee (models.Model):
    id = models.CharField(max_length=36, blank=False, primary_key=True)
    name = models.CharField(max_length=100, blank=False, default='Unknow')
    email = models.CharField(max_length=100, blank=False, unique=True)
    availability = models.CharField(max_length=1, blank=False, choices=Availability.choices,
                                    default=Availability.AVAILABLE)
