from rest_framework import serializers

from apps.employeemsg.models import EmployeeMessage


class EmployeeMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeMessage
        fields = ('id',
                  'idMessage',
                  'idEmployee',
                  'dateMessage',
                  'hourMessage',
                  'status')
