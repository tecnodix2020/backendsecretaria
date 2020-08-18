from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from user.models import User
from user.serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework_jwt.settings import api_settings

from rest_framework.permissions import AllowAny, IsAuthenticated

import uuid


# Get the users list
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def users_list(request):
    if request.method == 'GET':
        users = User.objects.all()

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_data['id'] = str(uuid.uuid4())
        user_serializer = UserSerializer(data=user_data)

        if user_serializer.is_valid():
            user_serializer.save()

            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def authenticate(request):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    if request.method == 'GET':
        user = User.objects.all()

        username = request.GET.get('username', None)
        password = request.GET.get('password', None)

        if username is not None and password is not None:
            user = user.filter(username=username)
            user = user.filter(password=password)

        user_serializer = UserSerializer(user, many=True)

        user = User(user_serializer.data)

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        response_data = {'user': user_serializer.data, 'auth_token': token}

        return JsonResponse(response_data, safe=False)
