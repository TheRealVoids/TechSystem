from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

import apps.common.services.mongodb.apps as CP
from apps.common.services.mongodb.models import Products
from apps.common.services.pgadmin.models import Opportunity

# Inicializar conexión con MongoDB
CP.initialize_mongo()


# Formulario para agregar una solicitud de arrendamiento
class LeaseRequestForm(forms.Form):
    notes = forms.CharField(
        label="Additional Notes",
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 4}),
    )


@login_required
def show_leases(request):
    return render(request, "layouts/leases.html")


@login_required
def add_lease_request(request):
    if request.method == "POST":
        # Programar esta parte

        return redirect("show_leases")  # Redirigir a la vista de arrendamientos
    else:
        form = LeaseRequestForm()

    # Obtener productos para mostrarlos como tarjetas
    products = Products.objects.all()

    # Convertir specific_attributes a un diccionario
    products_list = []
    categories_list = []
    for product in products:
        if product:
            # Convertir el product a un diccionario
            product_dict = product.to_mongo().to_dict()

            # Verificar si el producto tiene stock
            if product_dict.get("common_attributes", {}).get("stock", 0) > 0:
                products_list.append(product_dict)
                categories_list.append(product_dict.get("category"))
            else:
                print(
                    f"Producto {product_dict.get('common_attributes', {}).get('brand', '')} {product_dict.get('common_attributes', {}).get('model', '')} sin stock"
                )
        else:
            print("Producto no encontrado")

    return render(
        request,
        "layouts/add_lease_request.html",
        {"form": form, "products": products_list, "categories": categories_list},
    )
