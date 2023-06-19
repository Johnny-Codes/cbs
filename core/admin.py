from django.contrib import admin
from .models.sku import SKU


# Register your models here.
@admin.register(SKU)
class SKUAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "is_deleted",
    )
