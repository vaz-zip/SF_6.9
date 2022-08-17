from django.urls import path
from .views import room_view, message_create, message_detail, room_message_list, select_room, public_room_view


urlpatterns = [
    path('<str:pk>/room/', room_view, name='room_view'),
    path('message-create', message_create, name='message_create'),
    path('message-detail/<str:pk>/', message_detail, name='message_detail'),
    path('room-messages/<str:room_name>/', room_message_list, name='room-messages'),
    path('select-room', select_room, name="select_room"),
    path('public_room_view', public_room_view, name='public_room_view'),
]