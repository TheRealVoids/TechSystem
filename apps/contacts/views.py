from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import CharField, Q, TextField
from django.shortcuts import render

from apps.common.services.pgadmin.models import Contact


@login_required
def show_contacts(request):
    query = request.GET.get("query")
    contacts_list = Contact.objects.order_by("contact_id")

    if query:
        fields = [
            field.name
            for field in Contact._meta.get_fields()
            if isinstance(field, (CharField, TextField))
        ]

        query_filter = Q()
        for field in fields:
            query_filter |= Q(**{f"{field}__icontains": query})

        contacts_list = contacts_list.filter(query_filter)

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
