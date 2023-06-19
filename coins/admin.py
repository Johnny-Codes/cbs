from django.contrib import admin
from coins.models.silverdollars import SilverDollars, BulkSilverDollars


@admin.register(SilverDollars)
class SilverDollarsAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "__str__",
        "cost",
        "sale_price",
    )


@admin.register(BulkSilverDollars)
class BulkSilverDollarsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "sku",
        "__str__",
        "cost",
        "average_cost",
        "sale_price",
    )
