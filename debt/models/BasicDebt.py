from django.conf import settings
from django.db import models


class DebtQuerySet(models.QuerySet):
    def single(self):
        return self.filter(onesidedebt__is_null=False)

    def double(self):
        return self.filter(twosidesdebt__is_null=False)


class BasicDebt(models.Model):
    DEBT = 'D'
    CREDIT = 'C'
    ROLE_CHOICES = (
        (DEBT, 'debt'),
        (CREDIT, 'credit'),
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='debts')
    owner_role = models.CharField(max_length=1, choices=ROLE_CHOICES, default=CREDIT)

    amount = models.PositiveIntegerField()
    description = models.TextField()

    start_date = models.DateField()
    end_date = models.DateField()

    is_complete = models.BooleanField(default=False)

    objects = DebtQuerySet.as_manager()

    class Meta:
        db_table = 'basic_debt'
