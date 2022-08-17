from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100)


class Message(models.Model):
    text = models.CharField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True)
    room = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.text