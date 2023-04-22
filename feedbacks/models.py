from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from project.mixins.models import PKMixin


class Feedback(PKMixin):
    text = models.TextField(
        max_length=1024,
        null=True,
        blank=True
    )
    # Need to validate 1,2,3,4,5
    rating = models.PositiveSmallIntegerField(
        validators=(MaxValueValidator(5),)
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.PROTECT,
        related_name='feedbacks'
    )

    def __str__(self):
        return f"{self.user}. Rating {self.rating}. Text {self.text}"
