from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from api.models import Visits
from api.serializers import VisitsSerializer
from rest_framework.decorators import api_view

import uuid

@api_view(['GET', 'POST'])
def visits_list (request):
  if request.method == 'GET':
    visits = Visits.objects.all()

    visits_serializer = VisitsSerializer(visits, many=True)
    return JsonResponse(visits_serializer.data, safe=False)

  elif request.method == 'POST':
    visit_data = JSONParser().parse(request)
    visit_data['id'] = str(uuid.uuid4())
    print(visit_data)
    visit_serializer = VisitsSerializer(data=visit_data)

    if visit_serializer.is_valid():
      visit_serializer.save()

      return JsonResponse(visit_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(visit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
