from django.contrib.auth import get_user_model
from django.db import models
from django_lifecycle import LifecycleModelMixin

from project.mixins.models import PKMixin


class Favourite(LifecycleModelMixin, PKMixin):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    group = models.CharField(max_length=255)

    products = models.ForeignKey(
        'products.Product',
        on_delete=models.SET_NULL,
        related_name='favourites',
        null=True,
        blank=True
    )

    # def __str__(self):
    #     return f"User {self.user}. List {self.group} "
