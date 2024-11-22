from django.shortcuts import render

from apps.common.services.pgadmin.models import UserAccount


def show_users(request):
    users = UserAccount.objects.all()
    print(users)
    return render(request, "layouts/users.html", {"users": users})
