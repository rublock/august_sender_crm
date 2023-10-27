from django.contrib import admin
from .models import Client, Order, OrderPosition

admin.site.register(Client)


class OrderPositionInline(admin.TabularInline):
    model = OrderPosition
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [OrderPositionInline]
