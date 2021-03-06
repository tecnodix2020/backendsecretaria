import crypt
from email.utils import parseaddr
from hmac import compare_digest as compare_hash

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from apps.employee.serializers import EmployeeSerializer
from apps.user.models import User
from apps.user.serializers import UserSerializer
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
        user_saved = False
        user_data = JSONParser().parse(request)
        user_data['id'] = str(uuid.uuid4())
        if user_data['password']:
            user_data['password'] = crypt.crypt(user_data['password'])
        user_serializer = UserSerializer(data=user_data)

        if user_serializer.is_valid():
            if '@landix.com.br' in parseaddr(user_data['username'])[1]:
                user_serializer.save()
                user_saved = True
            else:
                return JsonResponse({'message': 'The email is invalid!'}, status=status.HTTP_401_UNAUTHORIZED)

        if user_saved:
            if post_employee(user_data):
                return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def post_employee(user_data):
    employee_data = {'id': user_data['id'], 'name': user_data['name'], 'email': user_data['username']}

    employee_serializer = EmployeeSerializer(data=employee_data)

    if employee_serializer.is_valid():
        employee_serializer.save()
        return True

    return False


# Authentication
@api_view(['POST'])
@permission_classes([AllowAny])
def authentication(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        plain_pass = user_data['password']
        user_data['password'] = crypt.crypt(user_data['password'])
        user = User.objects.filter(username=user_data['username']).values('id', 'name', 'username', 'password')

        if user and compare_hash(user[0]['password'], crypt.crypt(plain_pass, user[0]['password'])):
            user = user.values('id', 'name', 'username')
            user_serializer = UserSerializer(user, many=True)
            user = User(user_serializer.data)

            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)

            return JsonResponse({"user": user_serializer.data[0], 'auth_token': token},
                                status=status.HTTP_200_OK)
        else:
            return JsonResponse({"message": "Invalid username and/or password."},
                                safe=False,
                                status=status.HTTP_401_UNAUTHORIZED)
    else:
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'message': 'The user does not exists.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if request.method == 'GET':
        user_serializer = UserSerializer(user)
        return JsonResponse(user_serializer.data)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(user, data=user_data)
        print(user_serializer)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'User was deleted successfully.'})
