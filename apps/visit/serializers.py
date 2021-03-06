from rest_framework import serializers
from apps.visit.models import Visit


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('id',
                  'idEmployee',
                  'idVisitor',
                  'typeVisit',
                  'dateVisit',
                  'hourVisit',
                  'status',
                  'subs')
