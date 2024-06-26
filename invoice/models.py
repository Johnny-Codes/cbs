from django.db import models
from coins.models.coinbasemodel import CoinBaseModel
from customers.models import Customer
import stripe


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
    stripe_invoice_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    def create_stripe_invoice(self):
        customer = self.customer.stripe_id
        invoice = stripe.Invoice.create(
            customer=customer,
            collection_method="send_invoice",
            days_until_due=7,
            description=self.notes,
        )
        for item in self.sales_json["skus"]:
            print(item, type(item))
            inv_item = CoinBaseModel.objects.get(sku=item["sku"])
            if inv_item.stripe_product_id is None:
                inv_item.create_stripe_product()
            if inv_item.stripe_price_id is None:
                inv_item.create_stripe_price(sales_price=item["salesPrice"])
            original_sale_price = stripe.Price.retrieve(
                inv_item.stripe_price_id,
            ).unit_amount
            final_sale_price = item["salesPrice"] * 100
            print("og sales price", original_sale_price)
            print("final sale price", final_sale_price)
            if original_sale_price != item["salesPrice"]:
                inv_item.create_stripe_price(sales_price=item["salesPrice"])
            invoice_item = stripe.InvoiceItem.create(
                invoice=invoice["id"],
                customer=customer,
                price=inv_item.stripe_price_id,
                quantity=item["quantity"],
            )
            invoice["lines"]["data"].append(invoice_item)
        stripe.Invoice.finalize_invoice(invoice["id"])
        stripe.Invoice.send_invoice(invoice["id"])
        self.stripe_invoice_id = invoice["id"]
        self.save()
        return invoice

    def email_stripe_invoice(self):
        pass
