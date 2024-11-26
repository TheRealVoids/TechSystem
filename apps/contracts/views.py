from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import CharField, Q, TextField
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from apps.common.services.pgadmin.models import Contract, DeliveryCertificate


@csrf_exempt
def show_contracts(request):
    query = request.GET.get("query")
    contracts_list = Contract.objects.filter(nit=request.user.nit).order_by(
        "contract_id"
    )

    if query:
        fields = [
            field.name
            for field in Contract._meta.get_fields()
            if isinstance(field, (CharField, TextField))
        ]

        query_filter = Q()
        for field in fields:
            query_filter |= Q(**{f"{field}__icontains": query})

        contracts_list = contracts_list.filter(query_filter)

    paginator = Paginator(contracts_list, 10)
    page = request.GET.get("page")

    try:
        contracts = paginator.page(page)
    except PageNotAnInteger:
        contracts = paginator.page(1)
    except EmptyPage:
        contracts = paginator.page(paginator.num_pages)
    return render(request, "layouts/contracts.html", {"contracts": contracts})


@login_required
def show_delivery_certificates(request, contract_id):
    contract = Contract.objects.get(contract_id=contract_id)
    delivery_certificates = contract.deliverycertificate_set.all()
    return render(
        request,
        "layouts/delivery_certificates.html",
        {"delivery_certificates": delivery_certificates},
    )


@login_required
def show_equipments(request, certificate_id):
    certificate = DeliveryCertificate.objects.get(certificate_id=certificate_id)
    equipments = certificate.equipment_set.all()
    print(equipments.values())
    return render(
        request,
        "layouts/equipments.html",
        {"certificate": certificate, "equipments": equipments},
    )
