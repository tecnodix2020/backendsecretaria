import uuid

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny

from visitor.models import Visitor
from visitor.serializers import VisitorSerializer


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def visitors_list(request):
    if request.method == 'GET':
        visitors = Visitor.objects.all()
        visitors_serializer = VisitorSerializer(visitors, many=True)

        return JsonResponse(visitors_serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        visitor_data = JSONParser().parse(request)

        # Verify the personal code
        try:
            Visitor.objects.get(personalCode=visitor_data['personalCode'])
            return JsonResponse({'message': 'The personal code already exists.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        except Visitor.DoesNotExist:
            # Verify the email
            try:
                Visitor.objects.get(email=visitor_data['email'])
                return JsonResponse({'message': 'The email already exists.'},
                                    status=status.HTTP_406_NOT_ACCEPTABLE)
            except Visitor.DoesNotExist:
                visitor_data['id'] = str(uuid.uuid4())
                visitor_serializer = VisitorSerializer(data=visitor_data)

                if visitor_serializer.is_valid():
                    visitor_serializer.save()
                    return JsonResponse(visitor_serializer.data, status=status.HTTP_201_CREATED)

                return JsonResponse(visitor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def visitor_detail(request, pk):
    try:
        visitor = Visitor.objects.get(pk=pk)
    except Visitor.DoesNotExist:
        return JsonResponse({'message': 'The visitor does not exists.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        visitor_serializer = VisitorSerializer(visitor)
        return JsonResponse(visitor_serializer.data)
    elif request.method == 'PUT':
        visitor_data = JSONParser().parse(request)
        visitor_serializer = VisitorSerializer(visitor, data=visitor_data)
        if visitor_serializer.is_valid():
            visitor_serializer.save()
            return JsonResponse(visitor_serializer.data)
        return JsonResponse(visitor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        visitor.delete()
        return JsonResponse({'message': 'Visitor was deleted successfully.'})
