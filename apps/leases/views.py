from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from apps.common.services.mongodb.models import (
    Products,
    RentalRequests,
    SpecificAttributes,
)
from apps.leases.forms import LeaseRequestForm


@login_required
def show_leases(request):
    user_company_nit = request.user.nit.nit
    leases_list = RentalRequests.objects.filter(customer_nit=user_company_nit)

    # Search functionality
    search_query = request.GET.get("search", "")
    if search_query:
        leases_list = leases_list.filter(customer_nit__icontains=search_query)

    # Pagination
    paginator = Paginator(leases_list, 10)
    page = request.GET.get("page")
    try:
        leases = paginator.page(page)
    except PageNotAnInteger:
        leases = paginator.page(1)
    except EmptyPage:
        leases = paginator.page(paginator.num_pages)

    return render(
        request, "layouts/leases.html", {"leases": leases, "search_query": search_query}
    )


@login_required
def add_lease_request(request):
    if request.method == "POST":
        # Program this part

        return redirect("show_leases")  # Redirect to the leases view
    else:
        form = LeaseRequestForm()

    # Get products to display them as cards
    products = Products.objects.all()

    # Convert specific_attributes to a dictionary
    products_list = []
    categories_list = []
    for product in products:
        if product:
            # Convert the product to a dictionary
            product_dict = product.to_mongo().to_dict()

            # Check if the product has stock
            if int(product_dict.get("common_attributes", {}).get("stock", 0)) > 0:
                product_dict["id"] = str(product.id)  # Ensure product.id is a string
                products_list.append(product_dict)
                categories_list.append(product_dict.get("category"))
            else:
                print(
                    f"Product {product_dict.get('common_attributes', {}).get('brand', '')} {product_dict.get('common_attributes', {}).get('model', '')} out of stock"
                )
        else:
            print("Product not found")

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


@login_required
def show_lease_products(request, lease_id):
    lease = RentalRequests.objects.get(id=lease_id)
    products_details = []
    for item in lease.requested_equipment:
        product = Products.objects.get(id=item.product_id)
        product_dict = product.to_mongo().to_dict()
        product_dict["quantity"] = item.quantity
        products_details.append(product_dict)
    return render(
        request,
        "layouts/lease_products.html",
        {"lease": lease, "products": products_details},
    )


@login_required
def edit_lease(request, lease_id):
    product = Products.objects.get(id=lease_id)
    general_attributes = product.common_attributes

    if request.method == "POST":
        for key in general_attributes.keys():
            general_attributes[key] = request.POST.get(key, "N/A")
        product.common_attributes = general_attributes
        product.save()
        return redirect("leases:show_leases")

    return render(
        request,
        "layouts/edit_lease.html",
        {"lease_id": lease_id, "general_attributes": general_attributes},
    )


@login_required
def save_edit_lease(request, lease_id):
    lease = get_object_or_404(RentalRequests, id=lease_id)
    form = LeaseRequestForm(request.POST, instance=lease)

    if form.is_valid():
        form.save()
        return redirect("show_leases")

    return render(request, "layouts/edit_lease.html", {"form": form, "lease": lease})
