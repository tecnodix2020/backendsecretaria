from django.db import models
from utils.enumerators import Availability

class Users (models.Model):
  id = models.CharField(max_length=36, blank=False, primary_key=True)
  name = models.CharField(max_length=100, blank=False)
  email = models.CharField(max_length=100, blank=False, unique=True)
  username = models.CharField(max_length=100, blank=False, unique=True)
  password = models.CharField(max_length=100, blank=False, default='12345678')
  availability = models.CharField(max_length=1, blank=False, choices=Availability.choices, default=Availability.AVAILABLE)
