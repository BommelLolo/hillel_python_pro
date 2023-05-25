from django.contrib import admin

from products.models import Product, Category
from project.mixins.admins import ImageSnapshotAdminMixin


@admin.register(Product)
class ProductAdmin(ImageSnapshotAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'price', 'currency', 'price_uah',
                    "is_active", 'categories_list')
    filter_horizontal = ('categories', 'products')  # for parameters ManyToMany

    def categories_list(self, obj):
        return ', '.join(c.name for c in obj.categories.all())


@admin.register(Category)
class CategoryAdmin(ImageSnapshotAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'description', "is_active")
