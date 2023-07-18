from rest_framework import serializers
from coins.models.denominations import (
    CoinFamily,
    Denominations,
    CoinTypeName,
)
from coins.models.grading import (
    GradingServices,
    CoinGrades,
)
from coins.models.mints import SelectOneMint
from coins.models.strike import Strike


class CoinStrikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strike
        fields = ("id", "strike")


class CoinTypeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinTypeName
        fields = ("id", "coin_type")


class DenominationsSerializer(serializers.ModelSerializer):
    coin_type_name = CoinTypeNameSerializer(many=True)

    class Meta:
        model = Denominations
        fields = (
            "id",
            "denomination_of_coin",
            "coin_type_name",
        )


class CoinFamilySerializer(serializers.ModelSerializer):
    denominations = DenominationsSerializer(many=True)

    class Meta:
        model = CoinFamily
        fields = (
            "id",
            "type",
            "denominations",
        )


class GradingServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradingServices
        fields = (
            "id",
            "name",
        )


class CoinGradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinGrades
        fields = (
            "id",
            "grade",
        )


class SelectMintSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectOneMint
        fields = "__all__"
