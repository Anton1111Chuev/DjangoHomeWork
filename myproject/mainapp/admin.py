from django.contrib import admin
from .models import User, Product, Order, ItemsOrder


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'quantity', 'price', 'picture']
    list_filter = ['name', 'date_created', 'price', 'quantity']
    search_fields = ['description']
    actions = [reset_quantity]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price']


admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ItemsOrder)

# Register your models here.
