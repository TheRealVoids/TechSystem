from django.urls import path

from . import views

app_name = "leases"

urlpatterns = [
    path("", views.show_leases, name="show_leases"),
]
