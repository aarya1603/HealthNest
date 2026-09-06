from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.contact_list,
        name="contact_list"
    ),

    path(
        "delete/<int:contact_id>/",
        views.delete_contact,
        name="delete_contact"
    ),
]