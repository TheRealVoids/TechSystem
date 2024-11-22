from django.shortcuts import render

from apps.common.services.pgadmin.models import Contact


def show_contacts(request):
    contacts = Contact.objects.all()
    return render(request, "layouts/contacts.html", {"contacts": contacts})
