import datetime

from django.db import models

from utils.enumerators import StatusMessages


class EmployeeMessage(models.Model):
    id = models.CharField(max_length=36, blank=False, primary_key=True)
    idMessage = models.IntegerField(blank=False)
    idEmployee = models.CharField(max_length=36, blank=False)
    dateMessage = models.DateField(blank=False, default=datetime.date.today())
    hourMessage = models.TimeField(blank=False, default=datetime.time(12, 00))
    status = models.IntegerField(blank=False, choices=StatusMessages.choices,
                                 default=StatusMessages.UNREAD.value)
