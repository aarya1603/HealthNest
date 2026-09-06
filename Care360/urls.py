from django.contrib import admin
from django.urls import path, include
from Care360_homepage_be import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from subscriptions.views import subscription_page

urlpatterns = [

    path("accounts/", include("accounts.urls")),

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "",
        include("Care360_homepage_be.urls")
    ),

    path(
        "medicines/",
        include("medicines.urls")
    ),

    path(
        "emergency/",
        include("emergency.urls")
    ),

    path(
    "safety-care/",
    include("safetycare.urls")
),
path(
    "contact/", views.contact, name="contact"),



    path(
    "health/",
    include("healthprofile.urls")
),

    path(
        "reports/",
        include("reports.urls")
    ),

path(
    "insurance/",
    include("insurance.urls")
),
path(
    "checkups/",
    include("checkups.urls")
),

path(
    "trusted-contacts/",
    include("trustedcontacts.urls")
),
path(
    "subscription/",
    subscription_page,
    name="subscription",
),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

