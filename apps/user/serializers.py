from rest_framework import serializers
from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'name',
                  'username',
                  'password',
                  'appToken',
                  'availability')


class UserVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'name',
                  'username')
