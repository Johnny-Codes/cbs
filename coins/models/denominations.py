from django.db import models
from django.urls import reverse

FAMILY_CHOICES = (
    ("Gold", "Gold"),
    ("Silver", "Silver"),
    ("Clad", "Clad"),
    ("Nickel", "Nickel"),
    ("Copper", "Copper"),
)


class CoinFamily(models.Model):
    type = models.CharField(
        choices=FAMILY_CHOICES,
        max_length=20,
        unique=True,
    )

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "Coin Families"
        verbose_name = "Coin Family"


DENOM = (
    ("$50", "$50"),
    ("$25", "$25"),
    ("$20", "$20"),
    ("$10", "$10"),
    ("$5", "$5"),
    ("$4", "$4"),
    ("$3", "$3"),
    ("$2.5", "$2.5"),
    ("$1", "$1"),
    ("50C", "50C"),
    ("25C", "25C"),
    ("20C", "20C"),
    ("10C", "10C"),
    ("H10C", "H10C"),
    ("5C", "5C"),
    ("3CN", "3CN"),
    ("3CS", "3CS"),
    ("2C", "2C"),
    ("1C", "1C"),
    ("H1C", "H1C"),
)

GOLD_DENOM = (
    ("$20", "$20"),
    ("$10", "$10"),
    ("$5", "$5"),
    ("$4", "$4"),
    ("$3", "$3"),
    ("$2.5", "$2.5"),
    ("$1", "$1"),
)

SILVER_DENOM = (
    ("$1", "$1"),
    ("50C", "50C"),
    ("25C", "25C"),
    ("20C", "20C"),
    ("10C", "10C"),
    ("H10C", "H10C"),
    ("3CS", "3CS"),
)

COPPER_DENOM = (
    ("2C", "2C"),
    ("1C", "1C"),
    ("H1C", "H1C"),
)

NICKEL_DENOM = (
    ("5C", "5C"),
    ("3CN", "3CN"),
)

CLAD_DENOM = (
    ("$1", "$1"),
    ("50C", "50C"),
    ("25C", "25C"),
    ("10C", "10C"),
)


class Denominations(models.Model):
    denomination_of_coin = models.CharField(
        max_length=4,
        choices=DENOM,
        default="$1",
    )

    family = models.ForeignKey(
        CoinFamily,
        on_delete=models.CASCADE,
        related_name="denominations",
    )

    def __str__(self):
        return f"{self.family} {self.denomination_of_coin}"

    class Meta:
        verbose_name_plural = "Denominations"
        verbose_name = "Denomination"


class CoinTypeName(models.Model):
    coin_type = models.CharField(
        max_length=100,
    )
    denominations = models.ForeignKey(
        Denominations,
        on_delete=models.CASCADE,
        related_name="coin_type_name",
    )

    def get_url(self):
        return reverse("coins:coin_type_name", kwargs={"id": self.id})

    def __str__(self):
        return self.coin_type

    class Meta:
        verbose_name_plural = "Coin Type Names"
        verbose_name = "Coin Type Name"
