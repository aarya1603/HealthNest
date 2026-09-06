from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.emergency,
        name="emergency"
    ),

    path(
        "add/",
        views.add_emergency_contact,
        name="add_emergency_contact"
    ),

    path(
        "delete/<int:contact_id>/",
        views.delete_emergency_contact,
        name="delete_emergency_contact"
    ),


    path(
        "clear/",
        views.clear_emergency_contacts,
        name="clear_emergency_contacts"
    ),
    path(
    "review/",
    views.review,
    name="review"
),
]