from django.shortcuts import render
from django.utils import timezone

from apps.common.services.pgadmin.models import Contract


def index(request):
    now = timezone.now().date()
    last_contract = Contract.objects.order_by("-start_date").first()
    contracts_number = Contract.objects.count()
    expired_contracts_count = Contract.objects.filter(end_date__lt=now).count()
    active_contracts_count = Contract.objects.filter(
        end_date__gte=now
    ).count()  # Contratos activos

    context = {
        "user": request.user,
        "last_contract": last_contract,
        "contracts_number": contracts_number,
        "expired_contracts_count": expired_contracts_count,
        "active_contracts_count": active_contracts_count,
    }
    return render(request, "index.html", context)
