from django.contrib import admin
from django.utils.safestring import mark_safe

from products.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('preview', 'name', 'price', "is_active")
    filter_horizontal = ('categories', 'products')  # for parameters ManyToMany
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="60">')

# second variant instead decorator/ always in the end
# admin.register(Product, ProductAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', "is_active")
