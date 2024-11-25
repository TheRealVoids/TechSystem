from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("", views.show_users, name="show_users"),
    path(
        "company-details/",
        views.show_user_company_details,
        name="show_user_company_details",
    ),
]
