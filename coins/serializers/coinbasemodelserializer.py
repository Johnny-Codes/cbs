from coins.models.coinbasemodel import CoinBaseModel
from rest_framework import serializers


class CoinBaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinBaseModel
        fields = "__all__"


class CoinSkusOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinBaseModel
        fields = ["sku"]
