from django.db import models
from django.contrib.auth.models import User


BLOOD_GROUP_CHOICES = [
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("O+", "O+"),
    ("O-", "O-"),
    ("Unknown", "Unknown"),
]


class HealthProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="health_profile"
    )

    full_name = models.CharField(
        max_length=150,
        blank=True
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    blood_group = models.CharField(
        max_length=10,
        choices=BLOOD_GROUP_CHOICES,
        default="Unknown"
    )

    allergies = models.TextField(
        blank=True,
        help_text="List any known allergies."
    )

    medical_conditions = models.TextField(
        blank=True,
        help_text="List any existing medical conditions."
    )

    emergency_notes = models.TextField(
        blank=True,
        help_text="Important information that may be useful during an emergency."
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.full_name or self.user.username