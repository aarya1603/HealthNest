from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import HealthCheckup


@login_required
def checkup_list(request):

    if request.method == "POST":

        test_name = request.POST.get("test_name")
        test_date = request.POST.get("test_date")
        next_checkup_date = request.POST.get("next_checkup_date")
        notes = request.POST.get("notes")

        if test_name and test_date and next_checkup_date:

            HealthCheckup.objects.create(
                user=request.user,
                test_name=test_name,
                test_date=test_date,
                next_checkup_date=next_checkup_date,
                notes=notes
            )

            return redirect("checkup_list")

    checkups = HealthCheckup.objects.filter(
        user=request.user
    ).order_by("next_checkup_date")

    return render(
        request,
        "checkups/checkup_list.html",
        {
            "checkups": checkups
        }
    )