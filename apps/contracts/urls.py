from django.urls import path

from . import views

app_name = "contracts"

urlpatterns = [
    path("", views.show_contracts, name="show_contracts"),
    path(
        "<str:contract_id>/delivery_certificates/",
        views.show_delivery_certificates,
        name="show_delivery_certificates",
    ),
    path(
        "<str:certificate_id>/equipments/",
        views.show_equipments,
        name="show_equipments",
    ),
]
