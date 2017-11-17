from account.models import User
from account.serializers import FakeUserSerializer, UserSerializer

from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
