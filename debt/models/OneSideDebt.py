from .BasicDebt import BasicDebt
from django.db import models


class OneSideDebt(BasicDebt):
    stakeholder = models.ForeignKey('account.FakeUser', on_delete=models.PROTECT, related_name='debts')
    transfer_to = models.OneToOneField('debt.TwoSidesDebt', on_delete=models.SET_NULL, null=True, related_name='+')

    class Meta:
        db_table = 'one_side_debt'

    # TODO: Transfer to TwoSidesDebt when the transfer method of fake user is called
    def transfer(self, user):
        pass
