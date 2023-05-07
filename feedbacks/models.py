from django.core.cache import cache
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django_lifecycle import LifecycleModelMixin, hook, \
    AFTER_CREATE, AFTER_UPDATE

from project.mixins.models import PKMixin
from project.model_choices import FeedbackCacheKeys


class Feedback(LifecycleModelMixin, PKMixin):
    text = models.TextField(
        max_length=1024,
        null=True,
        blank=True
    )
    # Need to validate 1,2,3,4,5
    rating = models.PositiveSmallIntegerField(
        validators=(MaxValueValidator(5), MinValueValidator(0),)
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user}. Rating {self.rating}. Text {self.text}"

    @hook(AFTER_CREATE)
    @hook(AFTER_UPDATE)
    def after_signal(self):
        cache.delete(FeedbackCacheKeys.FEEDBACKS)
