from django.urls import path

from . import views

app_name = "leases"

urlpatterns = [
    path("", views.show_leases, name="show_leases"),
    path("add-lease-request/", views.add_lease_request, name="add_lease_request"),
]
