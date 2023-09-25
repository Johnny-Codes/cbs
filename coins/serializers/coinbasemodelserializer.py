from coins.models.coinbasemodel import CoinBaseModel
from coins.models.denominations import (
    CoinFamily,
    Denominations,
    CoinTypeName,
)
from coins.serializers.voserializers import (
    CoinFamilySerializer,
    CoinStrikeSerializer,
    DenominationsSerializer,
    CoinTypeNameSerializer,
)
from rest_framework import serializers


class CoinBaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinBaseModel
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        coin_family_id = data.get("family_of_coin")
        # not sure if I like this vs just putting it where it already exists.
        if coin_family_id is not None:
            try:
                coin_family = CoinFamily.objects.get(pk=coin_family_id)
                data["family_of_coin"] = CoinFamilySerializer(coin_family).data

                denom_data = data.get("denomination_of_coin")
                denominations = Denominations.objects.filter(pk=denom_data)
                data["family_of_coin"]["denominations"] = DenominationsSerializer(denominations, many=True).data

                coin_type_data = data.get("coin_type")
                coin_type_names = CoinTypeName.objects.filter(id=coin_type_data)
                data["family_of_coin"]["denominations"][0]["coin_type_name"] = CoinTypeNameSerializer(
                    coin_type_names, many=True
                ).data
            except CoinFamily.DoesNotExist:
                data["family_of_coin"] = None

        return data


class CoinSkusOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinBaseModel
        fields = ["sku"]
