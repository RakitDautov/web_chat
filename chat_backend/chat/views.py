from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from .serializers import RoomSerializer, ChatSerializer, ChatPostSerializer
from .models import Room, Chat


class RoomView(APIView):
    """Комнаты чатов"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        Room.objects.create(author=request.user, name=request.data['name'])
        return Response(status=status.HTTP_201_CREATED)


class ChatView(APIView):
    """Сообщения чата"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        room = request.GET.get("room")
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializer(chat, many=True)

        return Response({"data": serializer.data})

    def post(self, request):
        chat = ChatPostSerializer(data=request.data)
        if chat.is_valid():
            chat.save(user=request.user)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
