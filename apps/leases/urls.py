from django.urls import path

from . import views

app_name = "leases"

urlpatterns = [
    path("", views.show_leases, name="show_leases"),
    path("add-lease-request/", views.add_lease_request, name="add_lease_request"),
    path(
        "<str:lease_id>/edit-specific-attributes/",
        views.edit_specific_attributes,
        name="edit_specific_attributes",
    ),
    path(
        "leases/<str:lease_id>/save-specific-attributes/",
        views.save_specific_attributes,
        name="save_specific_attributes",
    ),
    path(
        "<str:lease_id>/products/",
        views.show_lease_products,
        name="show_lease_products",
    ),
    path("<str:lease_id>/edit-lease/", views.edit_lease, name="edit_lease"),
    path("<str:lease_id>/save-edit/", views.save_edit_lease, name="save_edit_lease"),
]
