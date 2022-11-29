from django.urls import path

from . import views


urlpatterns = [
    path("room/", views.RoomView.as_view(), name="room"),
    path("chat/", views.ChatView.as_view(), name="chat")
]
