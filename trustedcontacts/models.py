
# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class TrustedContact(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="trusted_contacts"
    )

    name = models.CharField(
        max_length=100
    )

    relationship = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=20
    )

    email = models.EmailField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} ({self.relationship})"