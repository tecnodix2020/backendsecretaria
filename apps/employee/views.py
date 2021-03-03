from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from apps.employee.models import Employee
from apps.employee.serializers import EmployeeSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def employees_list(request):
    employees = Employee.objects.all()

    name = request.GET.get('name', None)

    if name is not None:
        employees = employees.filter(name__icontains=name)

    employees_serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse(employees_serializer.data, safe=False)
