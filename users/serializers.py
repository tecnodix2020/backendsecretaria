from rest_framework import serializers
from users.models import Users

class UsersSerializer (serializers.ModelSerializer):
  
  class Meta:
    model = Users
    fields = ('id',
              'name',
              'email',
              'username',
              'password',
              'availability')