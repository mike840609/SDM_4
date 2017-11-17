from django.shortcuts import render

from account.models import Friend
from account.serializers import FriendSerializer

from rest_framework import viewsets


class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
