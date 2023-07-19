from django.urls import path
from .views import SKUSerializerView, random_sku

urlpatterns = [
    path("sku/", SKUSerializerView.as_view()),
    path(
        "sku/random/",
        random_sku,
        name="random-sku",
    ),
]
