from django.urls import path
from .views.silverdollarserializerview import (
    SilverDollarsSerializerView,
    BulkSilverDollarsSerializerView,
    SilverDollarsDetailSerializerView,
    BulkSilverDollarsDetailSerializerView,
)

urlpatterns = [
    path("api/silverdollars/", SilverDollarsSerializerView.as_view()),
    path("api/silverdollars/<int:id>/", SilverDollarsDetailSerializerView.as_view()),
    path("api/bulksilverdollars/", BulkSilverDollarsSerializerView.as_view()),
    path("api/bulksilverdollars/<int:id>/", BulkSilverDollarsDetailSerializerView.as_view()),
]
