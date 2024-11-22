from django.shortcuts import render

from apps.common.services.pgadmin.models import Opportunity


def show_opportunities(request):
    opportunities = Opportunity.objects.all()
    return render(
        request, "layouts/opportunities.html", {"opportunities": opportunities}
    )
