from django.shortcuts import render

from apps.contracts.models import Contract


def index(request):
    last_contract = (
        Contract.objects.filter(user=request.user).order_by("-start_date").first()
    )  # Obtén el último contrato del usuario autenticado
    context = {
        "last_contract": last_contract,
    }
    return render(request, "index.html", context)
