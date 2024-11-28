from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from apps.common.services.mongodb.models import (
    Products,
    RentalRequests,
    RequestedEquipments,
    SpecificAttributes,
)
from apps.common.services.pgadmin.models import Category, CategorySpecificAttribute
from apps.leases.forms import LeaseRequestForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
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


@csrf_exempt
@login_required
def add_lease_request(request):
    if request.method == "POST":
        additional_notes = request.POST.get("additional_notes", "")
        requested_equipments = []

        # Process each product in the POST request
        for key, value in request.POST.items():
            if key.startswith("product-") and int(value) > 0:
                product_id = key.split("-")[1]
                quantity = int(value)
                requested_equipments.append(
                    RequestedEquipments(product_id=product_id, quantity=quantity)
                )

        # Create a new rental request
        rental_request = RentalRequests(
            customer_nit=request.user.nit.nit,
            requested_equipment=requested_equipments,
            status="pending",
        )
        rental_request.save()

        return redirect("leases:show_leases")
    else:
        form = LeaseRequestForm()

    products = Products.objects.all()
    products_list = []
    categories_list = [category.category_name for category in Category.objects.all()]
    for product in products:
        if product:
            product_dict = product.to_mongo().to_dict()
            if int(product_dict.get("common_attributes", {}).get("stock", 0)) > 0:
                product_dict["id"] = str(product.id)
                category_id = product_dict.get("category")
                category_name = Category.objects.get(
                    category_id=category_id
                ).category_name
                product_dict["category"] = category_name
                products_list.append(product_dict)
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

        # Convert specific_attributes to a dictionary if necessary
        if hasattr(specific_attributes, "to_mongo"):
            specific_attributes = specific_attributes.to_mongo().to_dict()
        else:
            specific_attributes = vars(specific_attributes)

        # Get the fields of the SpecificAttributes model
        available_fields = SpecificAttributes._fields.keys()
        # Filter the fields that are already present in specific_attributes
        available_fields = [
            field for field in available_fields if field not in specific_attributes
        ]

        # Filter the fields that are already present in specific_attributes

        # Filter available fields based on the product category
        category_specific_attributes = CategorySpecificAttribute.objects.filter(
            category_id_id=product.category
        ).values_list("attribute_id__attribute_name", flat=True)
        available_fields = [
            field for field in available_fields if field in category_specific_attributes
        ]

    except Products.DoesNotExist:
        return redirect("leases:show_leases")

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


@csrf_exempt
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

        return redirect("leases:add_lease_request")
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


@csrf_exempt
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
