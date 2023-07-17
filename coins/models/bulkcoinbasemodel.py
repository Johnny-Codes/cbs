from django.db import models
from coins.models.mints import SelectMints
from .coinbasemodel import CoinBaseModel
from ..data.grades import GRADES


class BulkCoinBaseModel(
    CoinBaseModel,
    SelectMints,
    models.Model,
):
    year_2 = models.IntegerField(blank=True, null=True)
    grade_2 = models.CharField(
        max_length=3,
        choices=GRADES,
        default="G",
        blank=True,
        null=True,
    )
    mint = None  # override mint from CoinBaseModel so we can use SelectMints

    def __str__(self):
        return f"{self.grade_1} {self.dollar_type} {self.denomination}"

    def average_cost(self):
        return self.cost / self.quantity

    # def add_cost(self, purchase_cost):
    #     self.cost += purchase_cost

    class Meta:
        abstract = True
