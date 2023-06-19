from django.urls import path
from .views.silverdollarserializerview import (
    SilverDollarsSerializerView,
    BulkSilverDollarsSerializerView,
    SilverDollarsDetailSerializerView,
    BulkSilverDollarsDetailSerializerView,
)
from .views.halfdollarviews import (
    HalfDollarsSerializerView,
    HalfDollarsDetailSerializerView,
    BulkHalfDollarsSerializerView,
    BulkHalfDollarsDetailSerializerView,
)

urlpatterns = [
    path(
        "api/silverdollars/",
        SilverDollarsSerializerView.as_view(),
    ),
    path(
        "api/silverdollars/<int:id>/",
        SilverDollarsDetailSerializerView.as_view(),
    ),
    path(
        "api/bulksilverdollars/",
        BulkSilverDollarsSerializerView.as_view(),
    ),
    path(
        "api/bulksilverdollars/<int:id>/",
        BulkSilverDollarsDetailSerializerView.as_view(),
    ),
    path(
        "api/halfdollars/",
        HalfDollarsSerializerView.as_view(),
    ),
    path(
        "api/halfdollars/<int:id>/",
        HalfDollarsDetailSerializerView.as_view(),
    ),
    path(
        "api/bulkhalfdollars/",
        BulkHalfDollarsSerializerView.as_view(),
    ),
    path(
        "api/bulkhalfdollars/<int:id>/",
        BulkHalfDollarsDetailSerializerView.as_view(),
    ),
]
