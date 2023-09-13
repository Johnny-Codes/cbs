from django.urls import path
from .views import sales_invoice

urlpatterns = [
    path("sales/invoice/", sales_invoice, name="sales_invoice"),
]
