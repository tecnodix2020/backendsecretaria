from django.db import models


# Availability
class Availability (models.TextChoices):
    AVAILABLE = '1'
    UNAVAILABLE = '0'


# Types visits
class TypesVisits (models.IntegerChoices):
    MEETING = 1
    PACKAGE = 2
    GENERAL = 3


# Status visits
class StatusVisits (models.IntegerChoices):
    SCHEDULED = 1
    STARTED = 2
    FINISHED = 3
    CANCELLED = 4


# Types message
class TypesMessages (models.IntegerChoices):
    MEETING = 1
    PACKAGE = 2
    GENERAL = 3


# Status Messages
class StatusMessages (models.IntegerChoices):
    UNREAD = 1
    READ = 2
