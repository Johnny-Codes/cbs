from django.db import models
import stripe
from core.models.createdupdated import CreatedUpdated
from core.models.isbulk import IsBulk
from core.models.sku import SKU
from core.models.softdelete import SoftDeleteModel
from coins.models.mints import (
    SelectOneMint,
)
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
from customers.models import Customer


class CoinBaseModel(
    SKU,
    CreatedUpdated,
    IsBulk,
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
    mint = models.ManyToManyField(
        SelectOneMint,
        related_name="mint",
        blank=True,
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
    grading = models.ManyToManyField(
        GradingServices,
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

    images = models.ManyToManyField(
        Images,
        blank=True,
    )
    strike = models.ForeignKey(
        Strike,
        on_delete=models.CASCADE,
    )
    stripe_product_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    stripe_price_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    def create_stripe_product(self):
        response = stripe.Product.create(
            name=self.title,
        )
        self.stripe_product_id = response["id"]
        self.save()
        return response

    def create_stripe_price(self, sales_price):
        response = stripe.Price.create(
            unit_amount=round(sales_price * 100),
            currency="usd",
            product=self.stripe_product_id,
        )
        self.stripe_price_id = response["id"]
        self.save()
        return response

    def __str__(self):
        return f"{self.year} {self.coin_type} {self.strike} {self.grade}"

    class Meta:
        verbose_name_plural = "Coin Base Models"
        verbose_name = "Coin Base Model"

    def update_quantity(self, method, qty):
        if method == "add":
            self.quantity += qty
        if method == "subtract":
            self.quantity -= qty
        self.save()
