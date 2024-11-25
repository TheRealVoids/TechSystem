from datetime import date

from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

import apps.common.services.mongodb.apps as CN
from apps.common.services.mongodb.models import (
    Products,
    RentalRequests,
    RequestedEquipments,
)
from apps.common.services.pgadmin.models import Contract


@csrf_exempt
def show_contracts(request):
    if request.method == "GET":
        # Consultar los contratos existentes
        contracts = Contract.objects.all()
        today = date.today()

        # Convertir contratos a una lista de diccionarios con estado calculado
        contract_list = []
        for contract in contracts:
            if contract.end_date < today:
                status = {"label": "Cerrado", "class": "bg-red-200 text-red-800"}
            elif contract.start_date > today:
                status = {"label": "Próximo", "class": "bg-yellow-200 text-yellow-800"}
            else:
                status = {"label": "Activo", "class": "bg-green-200 text-green-800"}

            # Agregar contrato con el estado calculado a la lista
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


@csrf_exempt
def create_contract(request):
    if request.method == "GET":
        # Consultar todos los productos disponibles en MongoDB
        CN.initialize_mongo()
        products = Products.objects.all()
        return render(request, "create_contract.html", {"products": products})

    elif request.method == "POST":
        # Procesar datos del formulario para crear un contrato
        customer_nit = request.POST.get("customer_nit")
        contract_products = request.POST.getlist("product_id")
        quantities = request.POST.getlist("quantity")

        # Crear lista de productos solicitados
        requested_equipment = []
        for product_id, quantity in zip(contract_products, quantities):
            requested_equipment.append(
                RequestedEquipments(product_id=product_id, quantity=int(quantity))
            )

        # Crear el contrato
        contract = RentalRequests(
            customer_nit=customer_nit,
            status="pending",
            requested_equipment=requested_equipment,
        )
        contract.save()

        return redirect("contracts")  # Redirige a la página de contratos
