from django.contrib import admin
from .models import Room, Chat


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """Комнаты чатов"""
    list_display = ("name", "author", "invited_user", "date")

    def invited_user(self, obj):
        return "\n".join([user.username for user in obj.invited.all()])


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    """Сообщения чатов"""
    list_display = ("room", "user", "text", "date")