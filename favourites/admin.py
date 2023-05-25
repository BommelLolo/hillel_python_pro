from django.contrib import admin

from favourites.models import Favourite
# from products.admin import ProductInline


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    ...
    # inlines = [ProductInline]
    # list_display = ('user', 'group')
