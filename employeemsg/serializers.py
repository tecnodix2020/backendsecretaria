from rest_framework import serializers

from employeemsg.models import EmployeeMessage


class EmployeeMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeMessage
        fields = ('id',
                  'idMessage',
                  'idEmployee',
                  'dateMessage',
                  'hourMessage',
                  'status')
