from django.shortcuts import render, redirect
from .models import Room, Message
from .serializers import MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from sign.models import Person


def room_view(request, pk):
    my_id = request.user.id
    new_room_name = ''
    my_person = Person.objects.get(user=request.user)
    if my_id < int(pk):
        new_room_name = str(my_id) + pk
    else:
        new_room_name = pk + str(my_id)

    if Room.objects.filter(name=new_room_name).exists():
        room = Room.objects.get(name=new_room_name)
        return render(request, 'room.html', {'room': room, 'user': request.user, 'person': my_person})
    else:
        room = Room.objects.create(name=new_room_name)
        room.save()
        return render(request, 'room.html', {'room': room, 'user': request.user, 'person': my_person})


@api_view(['POST'])
def message_create(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def message_detail(request, pk):
    tasks = Message.objects.get(id=pk)
    serializer = MessageSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def room_message_list(request, room_name):
    messages = Message.objects.filter(room=room_name)
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


def select_room(request):
    return render(request, 'select_chat.html')


def public_room_view(request):
    new_room_name = request.POST['room_name']
    my_person = Person.objects.get(user=request.user)

    if Room.objects.filter(name=new_room_name).exists():
        room = Room.objects.get(name=new_room_name)
        return render(request, 'room.html', {'room': room, 'user': request.user, 'person': my_person})
    else:
        room = Room.objects.create(name=new_room_name)
        room.save()
        return render(request, 'room.html', {'room': room, 'user': request.user, 'person': my_person})


