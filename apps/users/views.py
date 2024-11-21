from django.shortcuts import render


def show_users(request):
    return render(request, "layouts/users.html")
