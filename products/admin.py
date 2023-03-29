from django.contrib import admin

from products.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', "is_active")
    filter_horizontal = ('categories', 'products')  # for parameters ManyToMany

# second variant instead decorator/ always in the end
# admin.register(Product, ProductAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', "is_active")
