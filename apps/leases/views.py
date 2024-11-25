from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def show_leases(request):
    return render(request, "layouts/leases.html")
