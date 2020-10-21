from django.http.response import JsonResponse
from fcm_django.models import FCMDevice
from rest_framework.parsers import JSONParser
from rest_framework import status

from user.models import User
from user.serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework_jwt.settings import api_settings

from rest_framework.permissions import AllowAny

import uuid


# Get the users list
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def users_list(request):
    if request.method == 'GET':
        users = User.objects.all()

        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_data['id'] = str(uuid.uuid4())
        user_serializer = UserSerializer(data=user_data)

        if user_serializer.is_valid():
            user_serializer.save()

            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Authentication
@api_view(['AUTH'])
@permission_classes([AllowAny])
def authentication(request):
    if request.method == 'AUTH':
        user_data = JSONParser().parse(request)
        user = User.objects.filter(username=user_data['username'],
                                   password=user_data['password']).values('id', 'name', 'email', 'username')

        user_serializer = UserSerializer(user, many=True)

        if user_serializer.data:
            user = User(user_serializer.data)

            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)

            return JsonResponse({"user": user_serializer.data, 'auth_token': token},
                                status=status.HTTP_200_OK)
        else:
            return JsonResponse({"message": "Invalid username and/or password."},
                                safe=False,
                                status=status.HTTP_401_UNAUTHORIZED)
    else:
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def notification(request):
    devices = FCMDevice.objects.all()
    print(devices)

    devices.send_message(title="Title", body="Message", data={"teste": "teste"})