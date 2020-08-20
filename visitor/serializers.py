from rest_framework import serializers

from visitor.models import Visitor


class VisitorSerializer (serializers.ModelSerializer):
    model = Visitor
    fields = ('id',
              'personalCode',
              'idCompany',
              'name',
              'email',
              'observation',
              'availability')
