from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.common.services.pgadmin.models import Contract, DeliveryCertificate


@login_required
def show_contracts(request):
    contracts = Contract.objects.filter(nit=request.user.nit)
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
