from django.db import models
from .coinbasemodel import CoinBaseModel
from .bulkcoinbasemodel import BulkCoinBaseModel
from accounts.models import Business
from core.models.sku import SKU


class HalfDollars(CoinBaseModel, models.Model):
    sku = models.ForeignKey(
        SKU,
        on_delete=models.CASCADE,
        related_name="half_dollar_sku",
    )
    denomination = models.CharField(max_length=3, default="50C")
    HALF_DOLLARS = (
        ("Flowing Hair Half Dollar", "Flowing Hair Half Dollar"),
        ("Draped Bust Half Dollar", "Draped Bust Half Dollar"),
        ("Capped Bust Half Dollar", "Capped Bust Half Dollar"),
        ("Liberty Seated Half Dollar", "Liberty Seated Half Dollar"),
        ("Barber Half Dollar", "Barber Half Dollar"),
        ("Walking Liberty Half Dollar", "Walking Liberty Half Dollar"),
        ("Kennedy Half Dollar", "Kennedy Half Dollar"),
    )
    half_dollar_type = models.CharField(max_length=30, choices=HALF_DOLLARS)
    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        related_name="half_dollars",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.year}-{self.mint} {self.half_dollar_type} {self.denomination} {self.grading} {self.strike} {self.grade}"

    class Meta:
        verbose_name_plural = "Half Dollars"
        verbose_name = "Half Dollar"


class BulkHalfDollars(BulkCoinBaseModel, models.Model):
    sku = models.ForeignKey(
        SKU,
        on_delete=models.CASCADE,
        related_name="bulk_half_dollar_sku",
    )
    denomination = models.CharField(max_length=3, default="50C")
    HALF_DOLLARS = (
        ("Flowing Hair Half Dollar", "Flowing Hair Half Dollar"),
        ("Draped Bust Half Dollar", "Draped Bust Half Dollar"),
        ("Capped Bust Half Dollar", "Capped Bust Half Dollar"),
        ("Liberty Seated Half Dollar", "Liberty Seated Half Dollar"),
        ("Barber Half Dollar", "Barber Half Dollar"),
        ("Walking Liberty Half Dollar", "Walking Liberty Half Dollar"),
        ("Kennedy Half Dollar", "Kennedy Half Dollar"),
    )
    half_dollar_type = models.CharField(max_length=30, choices=HALF_DOLLARS)
    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        related_name="bulk_half_dollars",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.grade_1} {self.half_dollar_type} {self.denomination}"

    class Meta:
        verbose_name_plural = "Bulk Half Dollars"
        verbose_name = "Bulk Half Dollars"
