from rest_framework import serializers
from api.models import Visits

class VisitsSerializer (serializers.ModelSerializer):
  class Meta:
    model = Visits
    fields = ('id',
              'idEmployee',
              'idTypeVisit',
              'idVisitor',
              'dateVisit',
              'hourVisit',
              'status')