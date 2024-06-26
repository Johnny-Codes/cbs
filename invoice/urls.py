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
        name="all_sales_invoice_for_customer",
    ),
    path(
        "sales/invoice/customer/<int:customer_id>/<int:sales_invoice_id>",
        SalesInvoiceForCustomerView.as_view(),
        name="single_sales_invoice_for_customer",
    ),
]
