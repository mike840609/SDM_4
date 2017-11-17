from rest_framework import viewsets

from account.models import FakeUser
from account.serializers import FakeUserSerializer


class FakeUserViewSet(viewsets.ModelViewSet):
    queryset = FakeUser.objects.all()
    serializer_class = FakeUserSerializer
