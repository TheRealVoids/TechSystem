from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.common.services.mongodb.models import RentalRequests


@login_required
def show_leases(request):
    leases = RentalRequests.objects.all()
    return render(request, "layouts/leases.html", {"leases": leases})
