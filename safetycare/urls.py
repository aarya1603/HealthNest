from django.urls import path
from . import views


urlpatterns = [
    path("", views.safetycare, name="safetycare"),
]