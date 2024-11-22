from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

from apps.common.services.pgadmin.models import UserAccount

from .backends import UserAccountBackend
from .forms import LoginForm


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            backend = UserAccountBackend()
            user = backend.authenticate(request, username=username, password=password)
            if user:
                login(
                    request,
                    user,
                    backend="apps.authentication.backends.UserAccountBackend",
                )
                return redirect("index")
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, "layouts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("index")
