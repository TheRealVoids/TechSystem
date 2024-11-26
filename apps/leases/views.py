from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.common.services.mongodb.models import Products, RentalRequests
from apps.leases.forms import LeaseRequestForm


@login_required
def show_leases(request):
    leases = RentalRequests.objects.all()
    print(leases)
    return render(request, "layouts/leases.html", {"leases": leases})


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
