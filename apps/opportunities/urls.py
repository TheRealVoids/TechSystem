from django.urls import path

from . import views

urlpatterns = [
    path("", views.show_opportunities, name="show_opportunities"),
]
