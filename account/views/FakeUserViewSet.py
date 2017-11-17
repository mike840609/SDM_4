from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from account.models import FakeUser
from account.serializers import FakeUserSerializer


class FakeUserViewSet(viewsets.ModelViewSet):
    queryset = FakeUser.objects.all()
    serializer_class = FakeUserSerializer

    def list(self, request, owner_pk=None):
        queryset = FakeUser.objects.filter(owner=owner_pk)
        serializer = FakeUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, owner_pk=None):
        queryset = FakeUser.objects.filter(pk=pk, owner=owner_pk)
        fake_user = get_object_or_404(queryset, pk=pk)
        serializer = FakeUserSerializer(fake_user)
        return Response(serializer.data)

    # TODO: Add a method for assigning debts of a fake user to a real user
    @detail_route(methods=['post'], url_name='assign')
    def assign(self, request, pk=None, owner_pk=None):
        pass
