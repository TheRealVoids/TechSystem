from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render

from apps.common.services.mongodb.models import Products, RentalRequests
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
            if product_dict.get("common_attributes", {}).get("stock", 0) > 0:
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
