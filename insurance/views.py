from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import InsurancePolicy


@login_required
def insurance_list(request):

    if request.method == "POST":

        provider = request.POST.get("provider")
        policy_number = request.POST.get("policy_number")
        policy_type = request.POST.get("policy_type")
        start_date = request.POST.get("start_date")
        expiry_date = request.POST.get("expiry_date")
        coverage_amount = request.POST.get("coverage_amount")
        policy_document = request.FILES.get("policy_document")

        if (
            provider
            and policy_number
            and policy_type
            and start_date
            and expiry_date
        ):

            InsurancePolicy.objects.create(
                user=request.user,
                provider=provider,
                policy_number=policy_number,
                policy_type=policy_type,
                start_date=start_date,
                expiry_date=expiry_date,
                coverage_amount=coverage_amount or None,
                policy_document=policy_document
            )

            return redirect("insurance_list")

    policies = InsurancePolicy.objects.filter(
        user=request.user
    ).order_by("-expiry_date")

    return render(
        request,
        "insurance/insurance_list.html",
        {
            "policies": policies
        }
    )