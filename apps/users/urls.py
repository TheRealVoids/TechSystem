from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("", views.show_users, name="show_users"),
]
