from django.urls import path
from .views import SalesInvoiceSerializerView

urlpatterns = [
    path("sales/invoice/", SalesInvoiceSerializerView.as_view(), name="sales_invoice"),
]
