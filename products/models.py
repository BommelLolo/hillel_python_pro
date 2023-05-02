from os import path

from django.core.cache import cache
from django.db import models
from django.core.validators import MinValueValidator
from django_lifecycle import LifecycleModelMixin, hook, \
    AFTER_UPDATE, AFTER_CREATE

from project.constants import DECIMAL_PLACES, MAX_DIGITS
from project.mixins.models import PKMixin


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

    def __str__(self):
        return f"{self.name} --- Price {self.price}"

    @hook(AFTER_CREATE)
    @hook(AFTER_UPDATE)
    def set_total_amount(self):
        cache.remove()
