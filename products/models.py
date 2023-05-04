from os import path

from django.core.cache import cache
from django.db import models
from django.core.validators import MinValueValidator
from django_lifecycle import LifecycleModelMixin, hook, \
    AFTER_UPDATE, AFTER_CREATE

from project.constants import DECIMAL_PLACES, MAX_DIGITS
from project.mixins.models import PKMixin
from project.model_choices import ProductCacheKeys, Currencies


def upload_to(instance, filename):
    _name, extension = path.splitext(filename)
    return f'products/images/{str(instance.pk)}{extension}'


class Category(LifecycleModelMixin, PKMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(
        blank=True,  # empty to Django
        null=True  # empty to db
    )
    image = models.ImageField(
        upload_to=upload_to,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(LifecycleModelMixin, PKMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to=upload_to,
        null=True,
        blank=True
    )
    sku = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category)
    products = models.ManyToManyField('products.Product', blank=True)
    # created_by
    price = models.DecimalField(
        validators=[MinValueValidator(0)],
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES
    )
    currency = models.CharField(
        choices=Currencies.choices,
        default=Currencies.UAH,
        max_length=16
    )

    def __str__(self):
        return f"{self.name} --- Price {self.price}"

    # def calc_price_UAH(self):
    #
    #     # Currencies(sorted(x.items(), key=lambda item: item[1]))
    #
    #     rate_usd = Currencies['']
    #
    #     if self.currency == Currencies.UAH:
    #         price_UAH = self.price
    #     elif self.currency == Currencies.USD:
    #         price_UAH = self.price
        #
        # if self.discount and self.discount.is_valid:
        #     if self.discount.discount_type == DiscountTypes.VALUE:
        #         total_amount -= self.discount.amount
        #     else:
        #         total_amount = total_amount * \
        #                        (1 - self.discount.amount / 100)

        # if self.discount and self.discount.is_valid:
        #     total_amount = (
        #         total_amount - self.discount.amount
        #         if self.discount.discount_type == DiscountTypes.VALUE else
        #         total_amount - (total_amount / 100 * self.discount.amount)
        #     ).quantize(decimal.Decimal('.01'))

        # return total_amount
    #
    # @hook(AFTER_UPDATE, when='discount', has_changed=True)
    # def set_total_amount(self):
    #     self.total_amount = self.get_total_amount()
    #     self.save(update_fields=('total_amount',), skip_hooks=True)

    @hook(AFTER_CREATE)
    @hook(AFTER_UPDATE)
    def after_signal(self):
        cache.delete(ProductCacheKeys.PRODUCTS)
