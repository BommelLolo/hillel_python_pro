from django.contrib import admin
from django.contrib.admin import TabularInline

from products.models import Product, Category
from project.mixins.admins import ImageSnapshotAdminMixin


class ProductInline(TabularInline):
    model = Product
    extra = 1


@admin.register(Product)
class ProductAdmin(ImageSnapshotAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'price', 'currency', 'price_uah',
                    "is_active", 'categories_list', 'created_at')
    filter_horizontal = ('categories', 'products')  # for parameters ManyToMany

    def categories_list(self, obj):
        return ', '.join(c.name for c in obj.categories.all())


@admin.register(Category)
class CategoryAdmin(ImageSnapshotAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'description', "is_active")
