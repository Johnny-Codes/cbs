from django.db import models
from .softdelete import SoftDeleteModel


class SKU(SoftDeleteModel, models.Model):
    sku = models.CharField(
        max_length=12,
        unique=True,
    )

    class Meta:
        app_label = "core"
        verbose_name_plural = "SKUs"
        verbose_name = "SKU"

    def __str__(self):
        return self.sku
