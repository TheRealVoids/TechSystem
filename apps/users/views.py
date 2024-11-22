from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.common.services.pgadmin.models import UserAccount


@login_required
def show_users(request):
    users = UserAccount.objects.all()
    return render(request, "layouts/users.html", {"users": users})
