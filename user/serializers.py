from rest_framework import serializers
from user.models import User, BlackListedToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'name',
                  'email',
                  'username',
                  'password',
                  'availability')


class BlackListedTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackListedToken
        fields = ('token',
                  'user',
                  'time')