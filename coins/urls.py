from django.urls import path
from coins.views import inventory_form_view

urlpatterns = [
    path("inventory/", inventory_form_view, name="inventory_form"),
]
