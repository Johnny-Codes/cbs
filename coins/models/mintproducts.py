from django.db import models
from core.models.createdupdated import CreatedUpdated
from core.models.isbulk import IsBulk
from core.models.sku import SKU
from coins.models.mints import (
    SelectOneMint,
)
from images.models import Images


class MintSetTypesModel(models.Model):
    mint_types = models.CharField(
        max_length=64,
        unique=True,
    )

    def __str__(self):
        return self.mint_types


class MintProductsModel(
    SKU,
    CreatedUpdated,
    IsBulk,
    models.Model,
):
    mint_set_type = models.ForeignKey(
        MintSetTypesModel,
        on_delete=models.CASCADE,
        related_name="mint_products",
    )
    title = models.CharField(
        max_length=80,
    )
    year = models.IntegerField()
    year2 = models.IntegerField(
        blank=True,
        null=True,
    )
    mint = models.ManyToManyField(
        SelectOneMint,
        related_name="mint_products",
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    cost = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        default=0,
    )
    quantity = models.IntegerField(default=1)
    sale_price = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        blank=True,
        null=True,
    )

    images = models.ManyToManyField(
        Images,
        blank=True,
    )
