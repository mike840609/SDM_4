from rest_framework import viewsets

from debt.models import BasicDebt
from debt.serializers import BasicDebtSerializer


class DebtViewSet(viewsets.ModelViewSet):
    queryset = BasicDebt.objects.all()
    serializer_class = BasicDebtSerializer
