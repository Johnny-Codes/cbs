from django.db import models
from accounts.models import Business
from coins.models.coinbasemodel import CoinBaseModel
from coins.models.bulkcoinbasemodel import BulkCoinBaseModel


class SilverDollars(CoinBaseModel, models.Model):
    SILVER_DOLLARS = (
        ("Flowing Hair Dollar", "Flowing Hair Dollar"),
        ("Draped Bust Dollar", "Draped Bust Dollar"),
        ("Liberty Seated Dollar", "Liberty Seated Dollar"),
        ("Trade Dollar", "Trade Dollar"),
        ("Morgan Dollar", "Morgan Dollar"),
        ("Peace Dollar", "Peace Dollar"),
        ("Ike Dollar", "Ike Dollar"),
        ("Susan B. Anthony Dollar", "Susan B. Anthony Dollar"),
        ("Sacagawea Dollar", "Sacagawea Dollar"),
        ("Presidential Dollar", "Presidential Dollar"),
        ("American Innovation Dollar", "American Innovation Dollar"),
    )
    dollar_type = models.CharField(max_length=30, choices=SILVER_DOLLARS)
    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        related_name="silver_dollars",
        null=True,
        blank=True,
    )

    def __str__(self):
        return (
            f"{self.year}-{self.mint} {self.dollar_type} {self.denomination} {self.grading} {self.strike} {self.grade}"
        )

    class Meta:
        verbose_name_plural = "Silver Dollars"
        verbose_name = "Silver Dollar"


class BulkSilverDollars(BulkCoinBaseModel, models.Model):
    SILVER_DOLLARS = (
        ("Flowing Hair Dollar", "Flowing Hair Dollar"),
        ("Draped Bust Dollar", "Draped Bust Dollar"),
        ("Liberty Seated Dollar", "Liberty Seated Dollar"),
        ("Trade Dollar", "Trade Dollar"),
        ("Morgan Dollar", "Morgan Dollar"),
        ("Peace Dollar", "Peace Dollar"),
        ("Ike Dollar", "Ike Dollar"),
        ("Susan B. Anthony Dollar", "Susan B. Anthony Dollar"),
        ("Sacagawea Dollar", "Sacagawea Dollar"),
        ("Presidential Dollar", "Presidential Dollar"),
        ("American Innovation Dollar", "American Innovation Dollar"),
    )
    dollar_type = models.CharField(max_length=30, choices=SILVER_DOLLARS)
    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        related_name="bulk_silver_dollars",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.grade_1} {self.dollar_type} {self.denomination}"

    class Meta:
        verbose_name_plural = "Bulk Silver Dollars"
        verbose_name = "Bulk Silver Dollars"
