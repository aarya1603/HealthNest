from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.checkup_list,
        name="checkup_list"
    ),
]