from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import Sum, F
from django.utils import timezone

from project.constants import DECIMAL_PLACES, MAX_DIGITS
from project.mixins.models import PKMixin
from project.model_choices import DiscountTypes


User = get_user_model()


class Discount(PKMixin):
    is_active = models.BooleanField(
        default=True
    )
    code = models.CharField(
        max_length=32,
        unique=True
    )
    total_amount = models.DecimalField(
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES
    )
    discount_type = models.PositiveSmallIntegerField(
        choices=DiscountTypes.choices,
        default=DiscountTypes.VALUE
    )
    valid_until = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"№{self.code} Discount: {self.total_amount} " \
               f"{DiscountTypes(self.discount_type).label}"

    @property
    def is_valid(self):
        is_valid = self.is_active
        if self.valid_until:
            is_valid &= (timezone.now() <= self.valid_until)
        return is_valid


class Order(PKMixin):
    order_number = models.PositiveSmallIntegerField(default=1)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    discount = models.ForeignKey(
        Discount,
        on_delete=models.PROTECT
        # null=True,
        # blank=True
    )
    is_paid = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    total_amount = models.DecimalField(
        validators=[MinValueValidator(0)],
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
        default=0
    )

    def __str__(self):
        return f"Order №{self.order_number} " \
               f"Amount: {self.total_amount}. User: {User}"

    # only one active order for user
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user'],
                                    condition=models.Q(is_active=True),
                                    name='unique_is_active')
        ]

    @property
    def is_current_order(self):
        return self.is_active and not self.is_paid

    def get_total_amount(self):
        total_amount = self.order_items.aggregate(
            total_amount=Sum(F('price') * F('quantity'))
        )['total_amount'] or 0

        if self.discount.is_active and self.discount.is_valid:
            if self.discount.discount_type == DiscountTypes.VALUE:
                total_amount -= self.discount.total_amount
            else:
                total_amount = total_amount * \
                               (1 - self.discount.total_amount / 100)
        return total_amount


class OrderItem(PKMixin):
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.PROTECT,
        related_name='order_items'
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        related_name='order_items',
        null=True
    )
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES
    )

    class Meta:
        unique_together = ('order', 'product')
