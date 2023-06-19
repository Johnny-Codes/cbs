from django.urls import path
from .views import SKUSerializerView

urlpatterns = [
    path("api/sku/", SKUSerializerView.as_view()),
]
