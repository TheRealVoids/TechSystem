from django.urls import path

from . import views

urlpatterns = [
    path("", views.show_leases, name="show_leases"),
]
