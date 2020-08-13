from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from api.models import Visits, Employees
from api.serializers import VisitsSerializer, EmployeesSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from utils.enumerators import TypesVisits

import uuid
import datetime

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def visits_list (request):
  if request.method == 'GET':
    visits = Visits.objects.all()

    date = request.GET.get('date', None)

    if date is not None:
      visits = visits.filter(dateVisit=date)

    typeVisit = request.GET.get('type', None)

    if typeVisit is not None:
      visits = visits.filter(idTypeVisit=typeVisit)

    visits_serializer = VisitsSerializer(visits, many=True)
    return JsonResponse(visits_serializer.data, safe=False)

  elif request.method == 'POST':
    visit_data = JSONParser().parse(request)
    visit_data['id'] = str(uuid.uuid4())
    visit_serializer = VisitsSerializer(data=visit_data)

    if visit_serializer.is_valid():
      visit_serializer.save()

      return JsonResponse(visit_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(visit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def visits_list_desk (request):
  visits = Visits.objects.get(dateVisit=datetime.date.today(), status=1)
  visits_serializer = VisitsSerializer(visits)

  return JsonResponse(visits_serializer.data, safe=False)

@api_view(['GET'])
def packages_list (request):
  packages = Visits.objects.get(idTypeVisit=TypesVisits.PACKAGE)
  visits_serializer = VisitsSerializer(packages)

  return JsonResponse(visits_serializer.data)

@api_view(['GET', 'PUT'])
def visit_detail (request, pk):
  try:
    visit = Visits.objects.get(pk=pk)
  except:
    return JsonResponse({'message': 'The visit does not exist'}, status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    visit_serializer = VisitsSerializer(visit)
    return JsonResponse(visit_serializer.data)
  elif request.method == 'PUT':
    visit_data = JSONParser.parse(request)
    visit_serializer = VisitsSerializer(visit, data=visit_data)

    if visit_serializer.is_valid():
      visit_serializer.save()
      return JsonResponse(visit_serializer.data)
    return JsonResponse(visit_serializer.errors, status=status.HTTP_400_BAD_REQUESTs)
