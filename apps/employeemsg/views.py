import uuid

from django.http import JsonResponse
from pyfcm import FCMNotification
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny

from apps.employeemsg.models import EmployeeMessage
from apps.employeemsg.serializers import EmployeeMsgSerializer
from apps.message.models import Message
from apps.message.serializers import MessageSerializer
from apps.user.models import User
from apps.user.serializers import UserSerializer


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
            if send_notification(message_serializer.validated_data):
                message_serializer.save()
                return JsonResponse(message_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({'message': 'Error sending the message to employee.'},
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return JsonResponse(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'message': 'The request is not valid.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def msg_emp_detail(request, pk):
    try:
        message = EmployeeMessage.objects.get(pk=pk)
    except EmployeeMessage.DoesNotExist:
        return JsonResponse({'message': 'The message does not exist.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if request.method == 'GET':
        message_serializer = EmployeeMsgSerializer(message)
        return JsonResponse(message_serializer.data)
    elif request.method == 'DELETE':
        message.delete()
        return JsonResponse({'message': 'The message was deleted successfully'}, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        message_data = JSONParser().parse(request)
        msg_load_serializer = EmployeeMsgSerializer(message)
        message_data['id'] = msg_load_serializer.data['id']
        message_data['idMessage'] = msg_load_serializer.data['idMessage']
        message_data['idEmployee'] = msg_load_serializer.data['idEmployee']
        message_serializer = EmployeeMsgSerializer(message, data=message_data)
        if message_serializer.is_valid():
            message_serializer.save()
            return JsonResponse(message_serializer.data)
        return JsonResponse(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'message': 'The request is not valid.'}, status=status.HTTP_400_BAD_REQUEST)


def send_notification(message):
    api_key = "AAAAccrA1zw:APA91bGcvv22bjwPkOyzPFOgABqJfGKqaC3VGjM7MnwvsvGARE2swIRA_VpkqgjR_GjnEh72InzVLjd38Ftsj88mIYC6i-gRnVzlNbfkgqqqaEDGN8yesylP1KqgdhfV0eXo-KtdXuT7"
    if 'status' in message.keys():
        api_key = "AAAAlPTIg0E:APA91bFv2KHSDlS6d0kjxXt2ycwMjoOlwmzo2-JKGN0YT-iLy1d88HVvhKrK_tubJUcRDNU0UEg00_O4NkruIrchHN2dnWKxtkfm9qMa4Jzd8818S4CTNSRo82LPumXBWbxvpLNtmr0D"
        message['idEmployee'] = "c64c3a05-41c9-460d-8254-c80216195b97"
    push_service = FCMNotification(api_key=api_key)

    try:
        user = User.objects.get(id=message['idEmployee'])
        user_serializer = UserSerializer(user)
    except User.DoesNotExist:
        return JsonResponse({'message': 'The user does not exists.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    registration_id = user_serializer.data['appToken']

    try:
        message = Message.objects.get(id=message['idMessage'])
        message_serializer = MessageSerializer(message)
    except Message.DoesNotExist:
        return JsonResponse({'message': 'It is not possible to send the message, it does not exist.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    message_title = message_serializer.data['title']
    message_body = message_serializer.data['description']
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                               message_body=message_body)
    if result['success'] == 1:
        return True
    else:
        return False
