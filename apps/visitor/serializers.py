from rest_framework import serializers

from apps.visitor.models import Visitor


class VisitorSerializer (serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ('id',
                  'personalCode',
                  'idCompany',
                  'name',
                  'email',
                  'observation',
                  'availability')
