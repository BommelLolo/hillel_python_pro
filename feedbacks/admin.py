from django.contrib import admin

from feedbacks.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('text', 'rating', 'user')
    # list_display = ('product', 'user', 'rating', 'text')
