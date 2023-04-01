from django.contrib import admin

from orders.models import Order, OrderItem, Discount


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'amount', 'discount_type')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('number', 'total_amount', 'user', 'is_paid', 'is_active')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'price', 'order')
