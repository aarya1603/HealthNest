from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import HealthProfile
from .forms import HealthProfileForm


@login_required
def health_profile(request):

    profile, created = HealthProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        form = HealthProfileForm(
            request.POST,
            instance=profile
        )

        if form.is_valid():

            profile = form.save(
                commit=False
            )

            profile.user = request.user

            profile.save()

            return redirect("health_profile")

    else:

        form = HealthProfileForm(
            instance=profile
        )

    return render(
        request,
        "healthprofile/profile.html",
        {
            "form": form,
            "profile": profile
        }
    )