from django.db import models
from .softdelete import SoftDeleteModel
import random


def get_random_sku():
    return random.randint(0, 999999999999)


class SKU(SoftDeleteModel, models.Model):
    sku = models.CharField(
        max_length=12,
        unique=True,
        default=get_random_sku,
    )

    class Meta:
        app_label = "core"
        verbose_name_plural = "SKUs"
        verbose_name = "SKU"

    def __str__(self):
        return self.sku
