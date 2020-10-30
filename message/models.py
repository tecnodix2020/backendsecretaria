from django.db import models
from utils.enumerators import TypesMessages


class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    typeMessage = models.IntegerField(blank=False, choices=TypesMessages.choices,
                                      default=TypesMessages.GENERAL.value)
    description = models.CharField(max_length=300, blank=False)
