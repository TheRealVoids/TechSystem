from django import forms
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

import apps.common.services.mongodb.apps as CP
from apps.common.services.mongodb.models import Products, SpecificAttributes
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
                product_dict["id"] = str(product.id)  # Ensure product.id is a string
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


@login_required
def edit_specific_attributes(request, lease_id):
    try:
        product = Products.objects.get(id=lease_id)
        specific_attributes = product.specific_attributes

        # Convertir specific_attributes a un diccionario si es necesario
        if hasattr(specific_attributes, "to_mongo"):
            specific_attributes = specific_attributes.to_mongo().to_dict()
        else:
            specific_attributes = vars(specific_attributes)

        # Obtener los campos del modelo SpecificAttributes
        specific_attributes_fields = SpecificAttributes._fields.keys()

        # Filtrar los campos que ya están presentes en specific_attributes
        available_fields = [
            field
            for field in specific_attributes_fields
            if field not in specific_attributes
        ]

    except Products.DoesNotExist:
        return redirect("show_leases")

    return render(
        request,
        "layouts/edit_specific_attribute.html",
        {
            "lease_id": lease_id,
            "specific_attributes": specific_attributes,
            "available_fields": available_fields,
            "next": request.GET.get("next", "/"),
        },
    )


@login_required
def save_specific_attributes(request, lease_id):
    if request.method == "POST":
        specific_attributes = request.POST.getlist("specific_attributes[]")
        product = Products.objects.get(id=lease_id)

        # Crear una instancia de SpecificAttributes
        specific_attributes_dict = {
            key: value
            for key, value in zip(specific_attributes[::2], specific_attributes[1::2])
        }
        specific_attributes_instance = SpecificAttributes(**specific_attributes_dict)

        product.specific_attributes = specific_attributes_instance
        product.save()

        next_url = request.POST.get("next", reverse("index"))
        return redirect(next_url)
    else:
        return render(
            request, "layouts/edit_specific_attribute.html", {"lease_id": lease_id}
        )
