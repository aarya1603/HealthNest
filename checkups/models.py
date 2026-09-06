from django.db import models
from django.contrib.auth.models import User


class HealthCheckup(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="health_checkups"
    )

    test_name = models.CharField(
        max_length=200
    )

    test_date = models.DateField()

    next_checkup_date = models.DateField()

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.test_name