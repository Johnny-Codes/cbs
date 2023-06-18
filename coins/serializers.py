from rest_framework import serializers
from coins.models import CoinInventory


class CoinInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinInventory
        fields = "__all__"
