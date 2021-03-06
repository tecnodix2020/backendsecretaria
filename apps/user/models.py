from django.db import models
from utils.enumerators import Availability


class User(models.Model):
    id = models.CharField(max_length=36, blank=False, primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    username = models.EmailField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=200, blank=False,
                                default='$6$cZhGoqXa69v81emH$GPWCx6zdcSL9XWeognIl.P0o5XhGQUFanL7q407rRp8X1st6zYphLMJPRLMHNFjCy8jAusw/636vr2TCnOIWH/')
    appToken = models.CharField(max_length=200, blank=True, unique=True)
    availability = models.CharField(max_length=1, blank=False, choices=Availability.choices,
                                    default=Availability.AVAILABLE)
