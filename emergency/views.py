from django.shortcuts import render, redirect, get_object_or_404

from .models import EmergencyContact


# =========================================================
# EMERGENCY CONTACT PAGE
# =========================================================

def emergency(request):

    contacts = EmergencyContact.objects.all().order_by("-id")

    print("EMERGENCY CONTACT COUNT:", contacts.count())

    print(
        "EMERGENCY CONTACTS:",
        list(
            contacts.values(
                "id",
                "name",
                "relationship",
                "phone"
            )
        )
    )

    return render(
        request,
        "emergency.html",
        {
            "emergency_contacts": contacts
        }
    )


# =========================================================
# ADD EMERGENCY CONTACT
# =========================================================

def add_emergency_contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        relationship = request.POST.get("relationship")
        phone = request.POST.get("phone")

        if name and relationship and phone:

            EmergencyContact.objects.create(
                name=name,
                relationship=relationship,
                phone=phone
            )

        return redirect("emergency")

    return render(
        request,
        "add_emergency_contact.html"
    )


# =========================================================
# DELETE EMERGENCY CONTACT
# =========================================================

def delete_emergency_contact(request, contact_id):

    if request.method == "POST":

        contact = get_object_or_404(
            EmergencyContact,
            id=contact_id
        )

        contact.delete()

    return redirect("emergency")

def clear_emergency_contacts(request):

    if request.method == "POST":

        EmergencyContact.objects.all().delete()

    return redirect("emergency")

# ============================================================
# REVIEW PAGE
# ============================================================

def review(request):

    success = False

    if request.method == "POST":

        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        rating = request.POST.get("rating", "").strip()
        review_text = request.POST.get("review", "").strip()

        if name and email and rating and review_text:

            email_subject = (
                f"Care360 Customer Review - {rating}/5 Stars"
            )

            email_message = f"""
NEW CARE360 CUSTOMER REVIEW
============================

Name:
{name}

Email:
{email}

Rating:
{rating}/5

Review:
{review_text}

============================
Sent from the Care360 website.
"""

            try:

                send_mail(
                    subject=email_subject,
                    message=email_message,
                    from_email=None,
                    recipient_list=[
                        "care360.c@gmail.com"
                    ],
                    fail_silently=False,
                )

                success = True

                print("================================")
                print("REVIEW EMAIL SENT SUCCESSFULLY")
                print("NAME:", name)
                print("EMAIL:", email)
                print("RATING:", rating)
                print("REVIEW:", review_text)
                print("================================")

            except Exception as e:

                print("================================")
                print("REVIEW EMAIL ERROR")
                print("ERROR TYPE:", type(e).__name__)
                print("ERROR:", str(e))
                print("================================")

    return render(
        request,
        "review.html",
        {
            "success": success
        }
    )