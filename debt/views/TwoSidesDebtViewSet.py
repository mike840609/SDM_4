from rest_framework import viewsets

from debt.models import TwoSidesDebt
from debt.serializers import TwoSidesDebtSerializer


class TwoSidesDebtViewSet(viewsets.ModelViewSet):
    queryset = TwoSidesDebt.objects.all()
    serializer_class = TwoSidesDebtSerializer
