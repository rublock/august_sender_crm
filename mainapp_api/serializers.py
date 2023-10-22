from rest_framework import serializers
from mainapp.models import OrderPosition


class OrderPositionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "order",
            "product",
            "client",
            "quantity",
            "description",
            "status",
            "created_at",
        )
        model = OrderPosition
