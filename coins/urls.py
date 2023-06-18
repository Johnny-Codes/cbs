from django.urls import path
from coins.views import add_inventory_api

urlpatterns = [
    path("add/", add_inventory_api),
]
