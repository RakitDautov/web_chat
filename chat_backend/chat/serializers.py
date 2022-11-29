from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Room, Chat


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""

    class Meta:
        model = User
        fields = ("id", "username")


class RoomSerializer(serializers.ModelSerializer):
    """Сериализация комнаты чата"""

    author = UserSerializer()
    invited = UserSerializer(many=True)

    class Meta:
        model = Room
        fields = ("id", "name", "author", "invited", "date",)


class ChatSerializer(serializers.ModelSerializer):
    """Сериализация сообщения"""

    user = UserSerializer()
    date = serializers.DateTimeField(format="%H:%M")
    

    class Meta:
        model = Chat
        fields = ("user", "text", "date")
        order_by = ('date', )


class ChatPostSerializer(serializers.ModelSerializer):
    """Сериализация сообщения"""

    class Meta:
        model = Chat
        fields = ("room", "text")
