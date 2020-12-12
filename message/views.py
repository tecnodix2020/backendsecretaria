from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from message.models import Message
from message.serializers import MessageSerializer


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def messages_list(request):
    if request.method == 'GET':
        type_message = request.GET.get('type', None)

        messages = Message.objects.all()

        if type_message is not None:
            messages = messages.filter(typeMessage=type_message)

        messages_serializer = MessageSerializer(messages, many=True)
        return JsonResponse(messages_serializer.data, safe=False)
    elif request.method == 'POST':
        message_data = JSONParser().parse(request)
        message_serializer = MessageSerializer(data=message_data)

        if message_serializer.is_valid():
            message_serializer.save()

            return JsonResponse(message_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def post_message(request):
    message_data = JSONParser().parse(request)
    message_serializer = MessageSerializer(data=message_data)

    if message_serializer.is_valid():
        message_serializer.save()

        return JsonResponse(message_serializer.data, status=status.HTTP_201_CREATED)

    return JsonResponse(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_message(request, pk):
    try:
        message = Message.objects.get(pk=pk)
    except Message.DoesNotExist:
        return JsonResponse({'message': 'The message does not exist.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    message.delete()
    return JsonResponse({'message': 'The message was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
