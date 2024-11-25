from django.urls import path

from . import views

app_name = "opportunities"

urlpatterns = [
    path("", views.show_opportunities, name="show_opportunities"),
    path(
        "<str:opportunity_id>/history/",
        views.show_opportunity_history,
        name="show_opportunity_history",
    ),
    path(
        "<str:opportunity_id>/services/",
        views.show_opportunity_services,
        name="show_opportunity_services",
    ),
]
