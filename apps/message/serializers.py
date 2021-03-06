from rest_framework import serializers
from apps.message.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id',
                  'typeMessage',
                  'title',
                  'description')
