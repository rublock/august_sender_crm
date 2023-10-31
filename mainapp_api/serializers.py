from rest_framework import serializers
from mainapp.models import OrderPosition, Client


class OrderPositionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "order",
            "product",
            "client",
            "quantity",
            "description",
            "status",
        )
        model = OrderPosition


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "name",
            "contact",
            "where_from",
            "oder_details",
            "address",
            "notes",
            "created_at",
        )
        model = Client
