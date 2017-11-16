from rest_framework import serializers

from account.models import User, Friend
from account.serializers import FakeUserSerializer, FriendSerializer


class UserSerializer(serializers.ModelSerializer):
    holders = FakeUserSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'name', 'password', 'holders', 'friends')
        extra_kwargs = {'password': {'write_only': True}}
