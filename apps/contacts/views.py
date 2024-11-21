from django.shortcuts import render


def show_contacts(request):
    return render(request, "layouts/contacts.html")
