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
    product_id = forms.ChoiceField(
        label="Available Products", widget=forms.Select(attrs={"class": "form-control"})
    )
    quantity = forms.IntegerField(
        label="Quantity",
        min_value=1,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    notes = forms.CharField(
        label="Additional Notes",
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 4}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Obtener productos de MongoDB y establecer opciones dinámicas
        products = Products.objects.all()
        self.fields["product_id"].choices = [
            (
                str(product.id),
                f"{product.common_attributes['brand']} {product.common_attributes['model']} ({product.category})",
            )
            for product in products
        ]


@login_required
def show_leases(request):
    return render(request, "layouts/leases.html")


@login_required
def add_lease_request(request):
    if request.method == "POST":
        form = LeaseRequestForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data["product_id"]
            quantity = form.cleaned_data["quantity"]
            notes = form.cleaned_data["notes"]

            # Obtener el producto seleccionado de MongoDB
            product = Products.objects.get(id=product_id)

            # Crear una nueva solicitud de arrendamiento (Opportunity)
            Opportunity.objects.create(
                nit=request.user.nit,  # Asociar la solicitud con la empresa del usuario
                contact_id=None,  # Si aplica, puedes enlazar al contacto específico
                opportunity_name=f"Lease Request: {product.common_attributes['brand']} {product.common_attributes['model']}",
                description=f"Quantity: {quantity}. Notes: {notes}",
                estimated_value=product.common_attributes["price"] * quantity,
                status="open",
                success_probability=0,
            )

            return redirect("show_leases")  # Redirigir a la vista de arrendamientos
    else:
        form = LeaseRequestForm()

    # Obtener productos para mostrarlos como tarjetas
    products = Products.objects.all()

    return render(
        request, "layouts/add_lease_request.html", {"form": form, "products": products}
    )
