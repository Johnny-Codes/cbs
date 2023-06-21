from django.db import models
from core.models.createdupdated import CreatedUpdated
from coins.models.mints import SelectOneMint
from images.models import Images
from .denominations import Denominations
from .strike import Strike
from ..data.grades import GRADES, GRADING_SERVICES


class CoinBaseModel(
    CreatedUpdated,
    SelectOneMint,
    Denominations,
    Strike,
    models.Model,
):
    pcgs_number = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=80)
    year = models.IntegerField()
    description = models.TextField(null=True, blank=True)

    grading = models.CharField(
        max_length=15,
        choices=GRADING_SERVICES,
        default="PCGS",
    )
    grade = models.CharField(max_length=3, choices=GRADES, default="70")
    cost = models.DecimalField(max_digits=11, decimal_places=2, default=0)
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

    def __str__(self):
        return f"{self.year}-{self.mint} {self.denomination} {self.grading} {self.strike} {self.grade}"

    class Meta:
        abstract = True
