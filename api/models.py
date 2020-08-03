from django.db import models

class Availability(models.TextChoices):
  AVAILABLE = '1'
  UNAVAILABLE = '0'

# Visits Class
class Visits (models.Model):
  # Types visits
  MEETING = 1
  PACKAGE = 2
  GENERAL = 3

  # Status visits
  SCHEDULED = 1
  STARTED = 2
  FINISHED = 3
  CANCELLED = 4

  TYPE_VISITS = [
    (MEETING, 'Meeting'),
    (PACKAGE, 'Package'),
    (GENERAL, 'General'),
  ]

  STATUS_VISITS = [
    (SCHEDULED, 'Scheduled'),
    (STARTED, 'Started'),
    (FINISHED, 'Finished'),
    (CANCELLED, 'Cancelled'),
  ]

  id = models.CharField(max_length=36, blank=False, primary_key=True)
  idEmployee = models.CharField(max_length=36, blank=False)
  idTypeVisit = models.IntegerField(blank=False, choices=TYPE_VISITS, default=MEETING)
  idVisitor = models.CharField(max_length=36, blank=True)
  dateVisit = models.DateTimeField(blank=False)
  status = models.IntegerField(blank=False, choices=STATUS_VISITS, default=SCHEDULED)

# Employees Class
class Employees (models.Model):
  id = models.CharField(max_length=36, blank=False, primary_key=True)
  name = models.CharField(max_length=100, blank=False)
  email = models.CharField(max_length=100, blank=False, unique=True)
  observation = models.CharField(max_length=200, blank=True, default='')
  availability = models.CharField(max_length=1, blank=False, choices=Availability.choices, default=Availability.AVAILABLE)

# Visitors class
class Visitors (models.Model):
  id = models.CharField(max_length=36, blank=False, primary_key=True)
  idCompany = models.CharField(max_length=36, blank=True)
  name = models.CharField(max_length=100, blank=False)
  email = models.CharField(max_length=100, blank=False, unique=True)
  cpf = models.CharField(max_length=11, blank=False, unique=True)
  observation = models.CharField(max_length=200, blank=True, default='')
  availability = models.CharField(max_length=1, blank=False, choices=Availability.choices, default=Availability.AVAILABLE)

# Companies class
class Companies (models.Model):
  id = models.CharField(max_length=36, blank=False, primary_key=True)
  companyName = models.CharField(max_length=100, blank=False)
  observation = models.CharField(max_length=200, blank=True, default='')
  availability = models.CharField(max_length=1, blank=False, choices=Availability.choices, default=Availability.AVAILABLE)