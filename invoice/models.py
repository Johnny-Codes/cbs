from django.db import models
from coins.models.coinbasemodel import CoinBaseModel
from customers.models import Customers


# Create your models here.
class SalesInvoice(models.Model):
    sales_item = models.ForeignKey(
        CoinBaseModel,
        related_name="sales",
        on_delete=models.CASCADE,
    )

    customer = models.ForeignKey(
        Customers,
        related_name="sales",
        on_delete=models.CASCADE,
    )

    invoice_date = models.DateTimeField(auto_now_add=True)

    notes = models.TextField(
        blank=True,
        null=True,
    )
