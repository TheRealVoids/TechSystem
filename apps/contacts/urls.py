from django.urls import path

from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.show_contacts, name="show_contacts"),
    path(
        "<str:contact_id>/interactions/",
        views.show_contact_interactions,
        name="show_contact_interactions",
    ),
    path(
        "<str:contact_id>/departments/",
        views.show_departments,
        name="show_departments",
    ),
]
