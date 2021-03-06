from django.db import models


class VisitSubs(models.Model):
    id = models.CharField(max_length=36, blank=False, primary_key=True)
    idVisit = models.CharField(max_length=36, blank=False)
    idEmployee = models.CharField(max_length=36, blank=True)
