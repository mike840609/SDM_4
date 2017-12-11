from .BasicDebt import BasicDebt
from django.conf import settings
from django.db import models


class TwoSidesDebt(BasicDebt):
    stakeholder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='related_debts')
    is_accepted = models.NullBooleanField(default=None)

    class Meta:
        db_table = 'two_sides_debt'
