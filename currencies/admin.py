from django.contrib import admin

from currencies.models import CurrencyHistory


@admin.register(CurrencyHistory)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'code', 'buy', "sale")
