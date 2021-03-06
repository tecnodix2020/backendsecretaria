from rest_framework import serializers
from apps.visitsubs.models import VisitSubs


class VisitSubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitSubs
        fields = ('id',
                  'idVisit',
                  'idEmployee')
