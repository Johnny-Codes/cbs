from django.urls import path

from .views import ImageSerializerView

urlpatterns = [
    path(
        "images/",
        ImageSerializerView.as_view(),
        name="image_api",
    )
]
