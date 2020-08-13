from rest_framework import serializers
from api.models import Visits, Employees

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

class EmployeesSerializer (serializers.ModelSerializer):
  class Meta:
    model = Employees,
    fields = ('id',
              'name',
              'email',
              'observation',
              'availability')