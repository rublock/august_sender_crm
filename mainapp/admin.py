from django.contrib import admin
from .models import Client, Product, Order, OrderPosition

admin.site.register(Client)
admin.site.register(Product)


class OrderPositionInline(admin.TabularInline):
    model = OrderPosition
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']
    inlines = [OrderPositionInline]
