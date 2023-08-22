from django.contrib import admin

from coins.models.denominations import (
    Denominations,
    CoinFamily,
    CoinTypeName,
)
from coins.models.coinbasemodel import CoinBaseModel
from coins.models.mints import SelectOneMint, SelectMints
from coins.models.strike import Strike
from coins.models.grading import (
    GradingServices,
    CoinGrades,
)
from coins.models.mintproducts import (
    MintSetTypesModel,
    MintProductsModel,
)


@admin.register(MintSetTypesModel)
class MintSetTypesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "mint_types",
    )


@admin.register(MintProductsModel)
class MintProducstAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
    )


@admin.register(GradingServices)
class GradingServicesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(CoinGrades)
class CoinGrades(admin.ModelAdmin):
    list_display = (
        "id",
        "grade",
    )


@admin.register(Strike)
class SelectStrikeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(SelectMints)
class SelectMintsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(SelectOneMint)
class SelectMintAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "coin_mint",
    )


@admin.register(CoinBaseModel)
class CoinBaseModel(admin.ModelAdmin):
    list_display = (
        "__str__",
        "quantity",
    )


@admin.register(CoinTypeName)
class CoinTypeNameAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "coin_type",
        "denomination",
    )

    def denomination(self, obj):
        return obj.denominations


@admin.register(Denominations)
class DenominationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "denomination_of_coin",
        "family",
    )

    def family(self, obj):
        return obj.family


@admin.register(CoinFamily)
class CoinFamilyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "type",
    )
