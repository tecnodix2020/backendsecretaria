from django.db import models
from djongo.models import ArrayField

from utils.enumerators import TypesVisits, StatusVisits

import datetime


class Visit(models.Model):
    id = models.CharField(max_length=36, blank=False, primary_key=True)
    idEmployee = models.CharField(max_length=36, blank=False)
    idVisitor = models.CharField(max_length=36, blank=True)
    typeVisit = models.IntegerField(blank=False, choices=TypesVisits.choices,
                                    default=TypesVisits.MEETING.value)
    dateVisit = models.DateField(blank=False, default=datetime.date.today())
    hourVisit = models.TimeField(blank=False, default=datetime.time(12, 00))
    status = models.IntegerField(blank=False, choices=StatusVisits.choices,
                                 default=StatusVisits.SCHEDULED.value)
