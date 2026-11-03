from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            auth_login(request, user)

            return redirect("health_profile")

    else:

        form = UserCreationForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("health_profile")

    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})