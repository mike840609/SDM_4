from django.contrib import admin

from debt.models import OneSideDebt, TwoSidesDebt


admin.site.register(OneSideDebt)
admin.site.register(TwoSidesDebt)
