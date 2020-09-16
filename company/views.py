import uuid

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny

from company.models import Company
from company.serializers import CompanySerializer


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def companies_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        availability = request.GET.get('availability', None)

        if availability is not None:
            companies = companies.filter(availability=availability)

        companies_serializer = CompanySerializer(companies, many=True)
        return JsonResponse(companies_serializer.data, safe=False)
    elif request.method == 'POST':
        company_data = JSONParser().parse(request)
        company_data['id'] = str(uuid.uuid4())
        company_serializer = CompanySerializer(data=company_data)

        if company_serializer.is_valid():
            company_serializer.save()

            return JsonResponse(company_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
