from django.db import models
from coins.models.coinbasemodel import CoinBaseModel
from customers.models import Customer


class SalesInvoice(models.Model):
    sales_item = models.ManyToManyField(
        CoinBaseModel,
        related_name="sales",
    )

    customer = models.ForeignKey(
        Customer,
        related_name="sales",
        on_delete=models.CASCADE,
    )

    invoice_date = models.DateTimeField(auto_now_add=True)
    sales_json = models.JSONField()
    notes = models.TextField(
        blank=True,
        null=True,
    )
