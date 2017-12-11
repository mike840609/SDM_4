from rest_framework import serializers

from account.serializers import UserSerializer
from debt.models import TwoSidesDebt


class TwoSidesDebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwoSidesDebt
        fields = '__all__'
