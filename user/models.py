from django.db import models
from rest_framework.permissions import BasePermission

from utils.enumerators import Availability


class User(models.Model):
    id = models.CharField(max_length=36, blank=False, primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False, unique=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False, default='12345678')
    availability = models.CharField(max_length=1, blank=False, choices=Availability.choices,
                                    default=Availability.AVAILABLE)


class BlackListedToken(models.Model):
    token = models.CharField(max_length=500)
    user = models.CharField(max_length=36, blank=False)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("token", "user")


class IsTokenValid(BasePermission):
    def has_permission(self, request, view):
        user_id = request.user.id
        is_allowed_user = True
        token = request.auth.decode("utf-8")

        try:
            is_blacklisted = BlackListedToken.objects.get(user=user_id, token=token)
            if is_blacklisted:
                is_allowed_user = False
        except BlackListedToken.DoesNotExist:
            is_allowed_user = True
        return is_allowed_user
