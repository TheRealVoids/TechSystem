from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from apps.common.services.pgadmin.models import Contact


@login_required
def show_contacts(request):
    contacts_list = Contact.objects.filter(nit=request.user.nit.nit).order_by(
        "last_name"
    )
    paginator = Paginator(contacts_list, 10)

    page = request.GET.get("page")
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

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
def show_contact_departments(request, contact_id):
    contact = Contact.objects.get(contact_id=contact_id)
    departments = contact.contactdepartment_set.all()
    return render(
        request,
        "layouts/contact_departments.html",
        {"contact": contact, "departments": departments},
    )
