from django.db import models
from django.contrib.auth.models import User


class InsurancePolicy(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="insurance_policies"
    )

    provider = models.CharField(
        max_length=200
    )

    policy_number = models.CharField(
        max_length=100
    )

    policy_type = models.CharField(
        max_length=100
    )

    start_date = models.DateField()

    expiry_date = models.DateField()

    coverage_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    policy_document = models.FileField(
        upload_to="insurance_documents/",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.provider} - {self.policy_number}"