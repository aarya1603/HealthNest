from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.health_profile,
        name="health_profile"
    ),

]