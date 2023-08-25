from django.urls import path
from accounts.views import (
    # user_list_api,
    # user_detail_api,
    # business_detail_api,
    # employees_of_business_api,
    BusinessListView,
)

urlpatterns = [
    # path("users/", user_list_api),
    # path("api/users/", UserListApi.as_view()),
    # path("users/<int:id>/", user_detail_api),
    path("businesses/", BusinessListView.as_view()),
    # path("businesses/<int:id>/", business_detail_api),
    # path("businesses/<int:id>/employees/", employees_of_business_api),
]
