from django.shortcuts import render


def show_opportunities(request):
    return render(request, "opportunities/opportunities.html")
