from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.common.services.pgadmin.models import Contact


@login_required
def show_contacts(request):
    contacts = Contact.objects.filter(nit=request.user.nit.nit)
    return render(request, "layouts/contacts.html", {"contacts": contacts})


@login_required
def show_contact_interactions(request, contact_id):
    contact = Contact.objects.get(contact_id=contact_id)
    interactions = contact.interaction_set.all()
    return render(
        request,
        "layouts/contact_interactions.html",
        {"contact": contact, "interactions": interactions},
    )


@login_required
def show_departments(request, contact_id):
    contact = Contact.objects.get(contact_id=contact_id)
    departments = contact.contactdepartment_set.all()
    return render(
        request,
        "layouts/contact_departments.html",
        {"contact": contact, "departments": departments},
    )
