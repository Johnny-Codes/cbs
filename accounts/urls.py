from django.urls import path
from accounts.views import (
    user_list_api,
    user_detail_api,
    business_list_api,
    business_detail_api,
    employees_of_business_api,
    UserListApi,
)

urlpatterns = [
    path("api/users/", user_list_api),
    # path("api/users/", UserListApi.as_view()),
    path("api/users/<int:id>/", user_detail_api),
    path("api/businesses/", business_list_api),
    path("api/businesses/<int:id>/", business_detail_api),
    path("api/businesses/<int:id>/employees/", employees_of_business_api),
]
