from django.shortcuts import render


def show_leases(request):
    return render(request, "layouts/leases.html")
