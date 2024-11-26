from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

import apps.common.services.mongodb.apps as CN
from apps.common.services.mongodb.models import (
    Products,
    RentalRequests,
    RequestedEquipments,
)
from apps.common.services.pgadmin.models import Contract, DeliveryCertificate


@csrf_exempt
def show_contracts(request):
    if request.method == "GET":
        contracts = Contract.objects.filter(nit=request.user.nit)
        today = date.today()

        contract_list = []
        for contract in contracts:
            if contract.end_date < today:
                status = {"label": "Cerrado", "class": "bg-red-200 text-red-800"}
            elif contract.start_date > today:
                status = {"label": "Próximo", "class": "bg-yellow-200 text-yellow-800"}
            else:
                status = {"label": "Activo", "class": "bg-green-200 text-green-800"}

            contract_list.append(
                {
                    "contract_id": contract.contract_id,
                    "contract_number": contract.contract_number,
                    "nit_id": contract.nit_id,
                    "monthly_value": contract.monthly_value,
                    "start_date": contract.start_date,
                    "end_date": contract.end_date,
                    "status": status,
                }
            )

        return render(request, "layouts/contracts.html", {"contracts": contract_list})


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
