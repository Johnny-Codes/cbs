from rest_framework import serializers
from ..models.sku import SKU


class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = [
            "id",
            "sku",
            "is_deleted",
        ]
