from django.contrib import admin
from invoice.models import SalesInvoice


# Register your models here.
@admin.register(SalesInvoice)
class SalesInvoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "invoice_date")
