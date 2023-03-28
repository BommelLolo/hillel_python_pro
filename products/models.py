from os import path

from django.db import models

from project.constants import DECIMAL_PLACES, MAX_DIGITS
from project.mixins.models import PKMixin


def upload_to(instance, filename):
    _name, extension = path.splitext(filename)
    return f'product/images/{str(instance.pk)}{extension}'


class Category(PKMixin):
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


class Product(PKMixin):
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
    sku = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, blank=True)
    products = models.ManyToManyField('products.Product', blank=True)
    # created_by
    price = models.DecimalField(
        max_digits=MAX_DIGITS,
        decimal_places=DECIMAL_PLACES
    )


class Discount(PKMixin):
    code = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    amount = models.PositiveIntegerField(default=0)

    type = models.CharField(
        max_length=16,
        choices=[(0, 'Money'), (1, 'Percents')]
    )
