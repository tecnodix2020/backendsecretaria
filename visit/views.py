from django.db.models import Count
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import json

from user.models import User
from user.serializers import UserSerializer, UserVisitSerializer
from visit.models import Visit
from visit.serializers import VisitSerializer

from visitor.models import Visitor
from visitor.serializers import VisitorSerializer

from employee.models import Employee
from employee.serializers import EmployeeSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from utils.enumerators import TypesVisits

import uuid
import datetime
from datetime import date

from visitsubs.serializers import VisitSubsSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_top3_of_visits(request):
    employees_list = []
    type_visit = request.GET.get('type', None)
    if type_visit is not None:
        visits = Visit.objects.values('idEmployee') \
            .filter(typeVisit=type_visit) \
            .annotate(num_visits=Count('idEmployee')) \
            .order_by('-num_visits')
    else:
        visits = Visit.objects.values('idEmployee').annotate(num_visits=Count('idEmployee')).order_by('-num_visits')

    length = 3
    if len(visits) <= 3:
        length = len(visits)

    for i in range(length):
        employees_list.append(visits[i]['idEmployee'])

    employees = Employee.objects.all()
    employees = employees.filter(id__in=employees_list)
    employees_serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse(employees_serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_visits_by_type(request):
    if request.GET.get('visitor', None) is not None:
        return get_visits_by_visitor(request)
    else:
        type_visits = request.GET.get('type', None)

        visits = Visit.objects.all()

        if type_visits is not None:
            visits = visits.filter(typeVisit=type_visits)

        visits_serializer = VisitSerializer(visits, many=True)

        return JsonResponse(visits_serializer.data, safe=False)


def get_visits_by_visitor(request):
    visitor_code = request.GET.get('visitor', None)

    visitor = Visitor.objects.all()
    visits = Visit.objects.all()
    visits = visits.filter(dateVisit=str(date.today()))
    visits = visits.filter(status=1)

    if visitor_code is not None:
        visitor = visitor.filter(personalCode=visitor_code)

    if not visitor:
        return JsonResponse({'message': 'Visitor not found.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    visitor_serializer = VisitorSerializer(visitor, many=True)
    visits = visits.filter(idVisitor=visitor_serializer.data[0]['id'])

    if not visits:
        return JsonResponse({'message': 'Visit not found for this visitor.'}, status=status.HTTP_204_NO_CONTENT)

    visits_serializer = VisitSerializer(visits, many=True)
    return JsonResponse(visits_serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_employees_waiting_packages(request):
    packages = Visit.objects.all().filter(typeVisit=2)
    visits_serializer = VisitSerializer(packages, many=True)
    employees = Employee.objects.all()
    employees_list = []

    for package in visits_serializer.data:
        employees_list.append(package['idEmployee'])

    employees = employees.filter(id__in=employees_list)
    employees_serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse(employees_serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_employees_visits(request):
    type_visit = request.GET.get('type', None)
    name = request.GET.get('name', None)

    if type_visit is None or name is None:
        return JsonResponse({'message': 'Request without parameters.'}, status=status.HTTP_400_BAD_REQUEST)

    visits = Visit.objects.all().filter(typeVisit=type_visit)

    visits_serializer = VisitSerializer(visits, many=True)
    employees = Employee.objects.all()
    employees_list = []

    for visit in visits_serializer.data:
        employees_list.append(visit['idEmployee'])

    employees = employees.filter(id__in=employees_list)

    employees = employees.filter(name__icontains=name)

    if not employees:
        return JsonResponse({'message': 'No visits found for this employee.'}, status=status.HTTP_204_NO_CONTENT)

    employees_serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse(employees_serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_employee_visit(request):
    name = request.GET.get('name', None)
    employees = Employee.objects.all()

    if name is not None:
        employees = employees.filter(name__icontains=name)
    else:
        return JsonResponse({'message': 'Not parameters.'}, status=status.HTTP_404_NOT_FOUND)

    employee_serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse(employee_serializer.data, safe=False)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def visits_list(request):
    if request.method == 'GET':
        visits = Visit.objects.all()

        date = request.GET.get('date', None)

        if date is not None:
            visits = visits.filter(dateVisit=date)

        type_visit = request.GET.get('type', None)

        if type_visit is not None:
            visits = visits.filter(idTypeVisit=type_visit)

        visits_serializer = VisitSerializer(visits, many=True)

        index = 0
        for visit in visits_serializer.data:
            visit['subs'] = json.loads(visit['subs'])
            for user_aux in visit['subs']:
                try:
                    user = User.objects.get(id=user_aux['id'])
                    user_serializer = UserVisitSerializer(user)
                    visit['subs'][index] = user_serializer.data
                    index = index + 1
                except User.DoesNotExist:
                    return JsonResponse({'message': 'The user does not exists.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return JsonResponse(visits_serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        visit_data = JSONParser().parse(request)
        visit_data['id'] = str(uuid.uuid4())

        index = 0
        for user_id in visit_data['subs']:
            try:
                user = User.objects.get(id=user_id)
                user_serializer = UserSerializer(user)
                visit_data['subs'][index] = user_serializer.data
                index = index + 1
            except User.DoesNotExist:
                return JsonResponse({'message': 'The user does not exists.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        visit_serializer = VisitSerializer(data=visit_data)
        if visit_serializer.is_valid():
            visit_serializer.save()
        else:
            return JsonResponse({'Object is not valid: ': visit_serializer.data, 'Errors: ': visit_serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse(visit_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse({'message': 'The request is not valid.'}, status=status.HTTP_400_BAD_REQUEST)


def save_sub_employees(id_visit, subs):
    result = False
    for sub in subs:
        sub_data = {'id': str(uuid.uuid4()), 'idVisit': id_visit, 'idEmployee': sub}
        visitsub_serializer = VisitSubsSerializer(data=sub_data)

        if visitsub_serializer.is_valid():
            visitsub_serializer.save()
            result = True
        result = False
    return result

    return False


@api_view(['GET'])
def visits_list_desk(request):
    visits = Visit.objects.get(dateVisit=datetime.date.today(), status=1)
    visits_serializer = VisitSerializer(visits)

    return JsonResponse(visits_serializer.data, safe=False)


@api_view(['GET'])
def packages_list(request):
    packages = Visit.objects.get(idTypeVisit=TypesVisits.PACKAGE)
    visits_serializer = VisitSerializer(packages)

    return JsonResponse(visits_serializer.data)


@api_view(['GET', 'PUT'])
def visit_detail(request, pk):
    try:
        visit = Visit.objects.get(pk=pk)
    except Visit.DoesNotExist:
        return JsonResponse({'message': 'The visit does not exist'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if request.method == 'GET':
        visit_serializer = VisitSerializer(visit)
        return JsonResponse(visit_serializer.data)
    elif request.method == 'PUT':
        visit_data = JSONParser.parse(request)
        visit_serializer = VisitSerializer(visit, data=visit_data)

        if visit_serializer.is_valid():
            visit_serializer.save()
            return JsonResponse(visit_serializer.data)
        return JsonResponse(visit_serializer.errors, status=status.HTTP_400_BAD_REQUESTs)
    else:
        return JsonResponse({'message': 'The request is not valid.'}, status=status.HTTP_400_BAD_REQUEST)
