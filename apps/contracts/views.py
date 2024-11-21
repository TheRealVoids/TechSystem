from django.shortcuts import render


def show_contracts(request):
    return render(request, "layouts/contracts.html")
