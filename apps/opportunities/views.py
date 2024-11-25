from django.shortcuts import render

from apps.common.services.pgadmin.models import Opportunity, OpportunityStageHistory


def show_opportunities(request):
    opportunities = Opportunity.objects.all()
    return render(
        request, "layouts/opportunities.html", {"opportunities": opportunities}
    )


def show_opportunity_history(request, opportunity_id):
    opportunity = Opportunity.objects.get(opportunity_id=opportunity_id)
    history = OpportunityStageHistory.objects.filter(
        opportunity_id=opportunity_id
    ).order_by("change_date")
    return render(
        request,
        "layouts/opportunity_history.html",
        {"opportunity": opportunity, "history": history},
    )
