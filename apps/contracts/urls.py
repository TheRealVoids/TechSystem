from django.urls import path

from . import views

app_name = "contracts"

urlpatterns = [
    path("", views.show_contracts, name="show_contracts"),
    path("create/", views.create_contract, name="create_contracts"),
]
