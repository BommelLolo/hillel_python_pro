from django.db import models

from project.constants import MAX_DIGITS, DECIMAL_PLACES
from project.mixins.models import PKMixin
from project.model_choices import Currencies


def get_usd_rate():
    return CurrencyHistory.objects.filter(
        code=Currencies.USD
    ).latest('created_at').sale


def get_euro_rate():
    return CurrencyHistory.objects.filter(
        code=Currencies.EUR
    ).latest('created_at').sale


class CurrencyHistory(PKMixin):
    code = models.CharField(
        choices=Currencies.choices,
        default=Currencies.UAH,
        max_length=16
    )

    buy = models.DecimalField(
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
        default=1
    )
    sale = models.DecimalField(
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
        default=1
    )

    def __str__(self):
        return f"{self.code}: {self.buy} / {self.sale}"
