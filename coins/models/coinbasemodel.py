from django.db import models
from core.models.createdupdated import CreatedUpdated
from core.models.softdelete import SoftDeleteModel
from coins.models.mints import SelectOneMint
from images.models import Images
from .denominations import (
    Denominations,
    CoinFamily,
    CoinTypeName,
)
from .strike import Strike
from coins.models.grading import (
    GradingServices,
    CoinGrades,
)


class CoinBaseModel(
    CreatedUpdated,
    SoftDeleteModel,
    models.Model,
):
    pcgs_number = models.IntegerField(
        null=True,
        blank=True,
    )
    title = models.CharField(
        max_length=80,
    )
    year = models.IntegerField()
    year2 = models.IntegerField(
        blank=True,
        null=True,
    )
    mint = models.ForeignKey(
        SelectOneMint,
        on_delete=models.CASCADE,
        related_name="mint",
    )
    description = models.TextField(null=True, blank=True)
    family_of_coin = models.ForeignKey(
        CoinFamily,
        on_delete=models.CASCADE,
        related_name="family_of_coin",
    )
    denomination_of_coin = models.ForeignKey(
        Denominations,
        on_delete=models.CASCADE,
        related_name="denomination_of_this_coin",
    )
    coin_type = models.ForeignKey(
        CoinTypeName,
        on_delete=models.CASCADE,
        related_name="coin_type_name",
    )
    grading = models.ForeignKey(
        GradingServices,
        on_delete=models.CASCADE,
        related_name="grading_service",
    )
    grade = models.ForeignKey(
        CoinGrades,
        on_delete=models.CASCADE,
        related_name="coin_grade",
    )
    grade2 = models.ForeignKey(
        CoinGrades,
        on_delete=models.CASCADE,
        related_name="coin_grade_2",
        blank=True,
        null=True,
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

    images = models.ForeignKey(
        Images,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    strike = models.ForeignKey(Strike, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.year}-{self.mint} {self.coin_type} {self.grading} {self.strike} {self.grade}"

    class Meta:
        verbose_name_plural = "Coin Base Models"
        verbose_name = "Coin Base Model"
