from django.urls import path
from .views import (
    SalesInvoiceSerializerView,
    SalesInvoiceForCustomerView,
)

urlpatterns = [
    path(
        "sales/invoice/",
        SalesInvoiceSerializerView.as_view(),
        name="sales_invoice",
    ),
    path(
        "sales/invoice/customer/<int:customer_id>",
        SalesInvoiceForCustomerView.as_view(),
        name="sales_invoice_for_customer",
    ),
]
