from rest_framework import views, status
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from account.models import User
from account.serializers import UserSerializer


class MeView(views.APIView):
    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(status=status.HTTP_200_OK,
                        data=serializer.data)
