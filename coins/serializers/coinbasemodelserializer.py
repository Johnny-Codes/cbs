from coins.models.coinbasemodel import CoinBaseModel
from coins.models.strike import Strike
from coins.models.mints import SelectOneMint
from coins.models.grading import GradingServices
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
    SelectMintSerializer,
    GradingServicesSerializer,
)
from rest_framework import serializers


class CoinBaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinBaseModel
        fields = "__all__"

    def validate_sku(self, value):
        if CoinBaseModel.objects.filter(sku=value).exists():
            raise serializers.ValidationError("SKU already exists")
        return value

    # need to add more error handling
    def to_representation(self, instance):
        data = super().to_representation(instance)
        coin_family_id = data.get("family_of_coin")
        if coin_family_id is not None:
            try:
                coin_family = CoinFamily.objects.get(pk=coin_family_id)
                data["family_of_coin"] = CoinFamilySerializer(coin_family).data

                denom_data = data.get("denomination_of_coin")
                denominations = Denominations.objects.filter(pk=denom_data)
                data["family_of_coin"]["denominations"] = DenominationsSerializer(
                    denominations, many=True
                ).data

                coin_type_data = data.get("coin_type")
                coin_type_names = CoinTypeName.objects.filter(id=coin_type_data)
                data["family_of_coin"]["denominations"][0]["coin_type_name"] = (
                    CoinTypeNameSerializer(coin_type_names, many=True).data
                )
            except CoinFamily.DoesNotExist:
                data["family_of_coin"] = None

        coin_strike_data = data.get("strike")
        coin_strike = Strike.objects.filter(id=coin_strike_data)
        data["strike"] = CoinStrikeSerializer(coin_strike, many=True).data

        coin_mint_data = data.get("mint")
        mint_list = []
        for mint in coin_mint_data:
            coin_mint = SelectOneMint.objects.filter(id=mint)
            mint_list.append(SelectMintSerializer(coin_mint, many=True).data)
        data["mint"] = mint_list

        coin_grading = data.get("grading")
        coin_grading_list = []
        for cg in coin_grading:
            coin_grade = GradingServices.objects.filter(id=cg)
            coin_grading_list.append(
                GradingServicesSerializer(coin_grade, many=True).data
            )
        data["grading"] = coin_grading_list

        return data


class CoinSkusOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinBaseModel
        fields = ["sku"]
