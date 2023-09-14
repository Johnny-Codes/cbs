from django.db import models
from coins.models.coinbasemodel import CoinBaseModel
from customers.models import Customers


class SalesInvoice(models.Model):
    sales_item = models.ManyToManyField(
        CoinBaseModel,
        related_name="sales",
    )

    customer = models.ManyToManyField(
        Customers,
        related_name="sales",
    )

    invoice_date = models.DateTimeField(auto_now_add=True)

    notes = models.TextField(
        blank=True,
        null=True,
    )
