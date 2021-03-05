from rest_framework import serializers
from apps.company.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id',
                  'companyName',
                  'observation',
                  'availability')
