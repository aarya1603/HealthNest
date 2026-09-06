from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import TrustedContact


@login_required
def contact_list(request):

    if request.method == "POST":

        name = request.POST.get("name")
        relationship = request.POST.get("relationship")
        phone = request.POST.get("phone")
        email = request.POST.get("email")

        if name and relationship and phone:

            TrustedContact.objects.create(
                user=request.user,
                name=name,
                relationship=relationship,
                phone=phone,
                email=email
            )

            return redirect("contact_list")

    contacts = TrustedContact.objects.filter(
        user=request.user
    ).order_by("name")

    return render(
        request,
        "trustedcontacts/contact_list.html",
        {
            "contacts": contacts
        }
    )
@login_required
def delete_contact(request, contact_id):

    contact = TrustedContact.objects.get(
        id=contact_id,
        user=request.user
    )

    contact.delete()

    return redirect("contact_list")