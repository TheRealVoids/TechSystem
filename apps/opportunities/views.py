from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from apps.common.services.pgadmin.models import (
    Opportunity,
    OpportunityProductService,
    OpportunityStageHistory,
)


@login_required
def show_opportunities(request):
    opportunities_list = Opportunity.objects.all().order_by("opportunity_id")
    paginator = Paginator(opportunities_list, 10)

    page = request.GET.get("page")
    try:
        opportunities = paginator.page(page)
    except PageNotAnInteger:
        opportunities = paginator.page(1)
    except EmptyPage:
        opportunities = paginator.page(paginator.num_pages)
    return render(
        request, "layouts/opportunities.html", {"opportunities": opportunities}
    )


@login_required
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


@login_required
def show_opportunity_services(request, opportunity_id):
    opportunity = Opportunity.objects.get(opportunity_id=opportunity_id)
    services = OpportunityProductService.objects.filter(opportunity_id=opportunity_id)
    return render(
        request,
        "layouts/opportunity_services.html",
        {"opportunity": opportunity, "services": services},
    )
