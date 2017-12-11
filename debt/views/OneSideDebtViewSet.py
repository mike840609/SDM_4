from rest_framework import viewsets

from debt.models import OneSideDebt
from debt.serializers import OneSideDebtSerializer


class OneSideDebtViewSet(viewsets.ModelViewSet):
    queryset = OneSideDebt.objects.all()
    serializer_class = OneSideDebtSerializer
