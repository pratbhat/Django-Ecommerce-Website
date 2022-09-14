from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'price')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'description')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'transaction_id', 'complete')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity')


class ShippingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order', 'address', 'state', 'city', 'zip_code')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAdmin)



