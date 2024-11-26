from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import CharField, F, Q, TextField
from django.shortcuts import render

from apps.common.services.pgadmin.models import Company, UserAccount


@login_required
def show_users(request):
    query = request.GET.get("query")
    users_list = UserAccount.objects.order_by("user_id")

    if query:
        fields = [
            field.name
            for field in UserAccount._meta.get_fields()
            if isinstance(field, (CharField, TextField))
        ]

        query_filter = Q()
        for field in fields:
            query_filter |= Q(**{f"{field}__icontains": query})

        users_list = users_list.filter(query_filter)

    for user in users_list:
        roles = user.userrole_set.select_related("role_id").values(
            _id=F("role_id__role_id"),
            role_name=F("role_id__role_name"),
            description=F("role_id__description"),
        )
        user.roles = list(roles)

    paginator = Paginator(users_list, 10)
    page = request.GET.get("page")

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, "layouts/users.html", {"users": users})


@login_required
def show_user_company_details(request):
    company = Company.objects.get(nit=request.user.nit.nit)
    return render(request, "layouts/user_company_details.html", {"company": company})
