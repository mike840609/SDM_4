from rest_framework import serializers

from debt.models import BasicDebt


class BasicDebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicDebt
        fields = '__all__'
