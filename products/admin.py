from django.contrib import admin

from products.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', "is_active")
    filter_horizontal = ('categories', 'products')  # for parameters ManyToMany

# admin.register(Product, ProductAdmin)  # second variant instead decorator/ always in the end


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    ...
