from django.contrib import admin
from coins.models.silverdollars import SilverDollars, BulkSilverDollars
from coins.models.halfdollars import HalfDollars, BulkHalfDollars


@admin.register(SilverDollars)
class SilverDollarsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "__str__",
        "cost",
        "sale_price",
    )


@admin.register(BulkSilverDollars)
class BulkSilverDollarsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "__str__",
        "cost",
        "quantity",
        "average_cost",
        "sale_price",
    )


@admin.register(HalfDollars)
class HalfDollarsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "__str__",
        "cost",
        "sale_price",
    )


@admin.register(BulkHalfDollars)
class BulkHalfDollarsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "__str__",
        "cost",
        "quantity",
        "average_cost",
        "sale_price",
    )
