import uuid

from django.http import JsonResponse
from pyfcm import FCMNotification
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny

from employeemsg.models import EmployeeMessage
from employeemsg.serializers import EmployeeMsgSerializer


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def msg_by_employee(request):
    if request.method == 'GET':
        id_employee = request.GET.get('employee', None)

        messages = EmployeeMessage.objects.all()

        if id_employee is not None:
            messages = messages.filter(idEmployee=id_employee)

        messages_serializer = EmployeeMsgSerializer(messages, many=True)
        return JsonResponse(messages_serializer.data, safe=False)
    elif request.method == 'POST':
        message_data = JSONParser().parse(request)
        message_data['id'] = str(uuid.uuid4())
        message_serializer = EmployeeMsgSerializer(data=message_data)

        if message_serializer.is_valid():
            message_serializer.save()
            return JsonResponse(message_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'message': 'The request is not valid.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes([AllowAny])
def msg_emp_detail(request, pk):
    try:
        message = EmployeeMessage.objects.get(pk=pk)
    except EmployeeMessage.DoesNotExist:
        return JsonResponse({'message': 'The message does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        message_serializer = EmployeeMsgSerializer(message)
        return JsonResponse(message_serializer.data)
    elif request.method == 'DELETE':
        message.delete()
        return JsonResponse({'message': 'The message was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return JsonResponse({'message': 'The request is not valid.'}, status=status.HTTP_400_BAD_REQUEST)


def send_notification(request):
    push_service = FCMNotification(api_key="AIzaSyDWOhxbvE3bDHLv8ymwRauWJOEM2EFkZ8I")
    registration_id = "<device registration_id>"
    message_title = "Uber update"
    message_body = "Hi john, your customized news for today is ready"
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                               message_body=message_body)
    print(result)
