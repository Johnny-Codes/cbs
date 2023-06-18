from django.urls import path
from accounts.views import (
    user_list_api,
    user_detail_api,
    business_list_api,
    business_detail_api,
)

urlpatterns = [
    path("api/users/", user_list_api),
    path("api/users/<int:id>", user_detail_api),
    path("api/businesses/", business_list_api),
    path("api/businesses/<int:id>", business_detail_api),
]
