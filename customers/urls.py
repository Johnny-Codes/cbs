from django.urls import path
from customers.views import (
    CustomersSerializerView,
    OneCustomerSerializerView,
)

urlpatterns = [
    path(
        "customers/",
        CustomersSerializerView.as_view(),
        name="customer_view",
    ),
    path(
        "customers/<int:id>/",
        OneCustomerSerializerView.as_view(),
        name="one_customer_view",
    ),
]
