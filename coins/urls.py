from django.urls import path
from coins.views.coinbasemodelview import (
    CoinBaseModelSerializerView,
    OneCoinBaseModelSerializerView,
    CoinTypeSerializerView,
    GetAllSkusView,
    pcgs_coin_data,
)
from coins.views.voviews import (
    CoinFamilySerializerView,
    GradingServicesSerializerView,
    CoinGradesSerializerView,
    SelectMintsSerializerView,
    CoinStrikeSerializer,
    DenominationSerializerView,
    CoinTypeNameSerializerView,
)

urlpatterns = [
    path(
        "coins/",
        CoinBaseModelSerializerView.as_view(),
        name="coin_base_model_serializer",
    ),
    path(
        "coins/<int:id>/",
        OneCoinBaseModelSerializerView.as_view(),
        name="one_coin_base_model",
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
    path(
        "coins/denominations/",
        DenominationSerializerView.as_view(),
        name="denominations",
    ),
    path(
        "coins/cointypes/",
        CoinTypeNameSerializerView.as_view(),
        name="coin_type_name",
    ),
    path(
        "coins/cointypes/<int:coin_type>/",
        CoinTypeSerializerView.as_view(),
        name="coin_type_name",
    ),
    path(
        "coins/skus/",
        GetAllSkusView.as_view(),
        name="get_all_skus",
    ),
    path(
        "coins/pcgs_coin_data/",
        pcgs_coin_data,
        name="pcgs_coin_data",
    ),
]
