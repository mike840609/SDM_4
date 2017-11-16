from django.shortcuts import render

from friend.models import Friend
from friend.serializers import FriendSerializer

from rest_framework import viewsets


class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer