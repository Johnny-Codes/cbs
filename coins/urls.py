from django.urls import path
from coins.views.coinbasemodelview import CoinBaseModelSerializerView
from coins.views.voviews import (
    CoinFamilySerializerView,
    GradingServicesSerializerView,
    CoinGradesSerializerView,
    SelectMintsSerializerView,
    CoinStrikeSerializer,
)

urlpatterns = [
    path(
        "coins/",
        CoinBaseModelSerializerView.as_view(),
        name="coin_base_model_serializer",
    ),
    path(
        "coins/family/",
        CoinFamilySerializerView.as_view(),
        name="coin_family",
    ),
    path(
        "coins/gradingservices/",
        GradingServicesSerializerView.as_view(),
        name="grading_services",
    ),
    path(
        "coins/coingrades/",
        CoinGradesSerializerView.as_view(),
        name="coin_grades",
    ),
    path(
        "coins/mints/",
        SelectMintsSerializerView.as_view(),
        name="select_mints",
    ),
    path(
        "coins/strike/",
        CoinStrikeSerializer.as_view(),
        name="coin_strike",
    ),
]
