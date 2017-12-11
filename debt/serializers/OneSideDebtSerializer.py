from rest_framework import serializers

from account.serializers import FakeUserSerializer, UserSerializer
from debt.models import OneSideDebt


class OneSideDebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneSideDebt
        fields = '__all__'
        excludes = ['transfer_to']
