from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.report_list,
        name="report_list"
    ),

    path(
        "summary/<int:report_id>/",
        views.report_summary,
        name="report_summary"
    ),

]