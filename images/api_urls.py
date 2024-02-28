from django.urls import path

from .views import ImageSerializerView, CoinImageView

urlpatterns = [
    path(
        "images/",
        ImageSerializerView.as_view(),
        name="image_api",
    ),
    path(
        "images/<int:id>/",
        CoinImageView.as_view(),
        name="single_image",
    ),
]
