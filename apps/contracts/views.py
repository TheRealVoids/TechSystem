from django.shortcuts import render

from apps.common.services.pgadmin.models import Contract


def show_contracts(request):
    contracts = Contract.objects.all()
    return render(request, "layouts/contracts.html", {"contracts": contracts})
