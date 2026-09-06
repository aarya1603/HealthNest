from django.db import models
from django.contrib.auth.models import User


class MedicalReport(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="medical_reports"
    )

    report_name = models.CharField(
        max_length=200
    )

    report_date = models.DateField(
        null=True,
        blank=True
    )

    report_file = models.FileField(
        upload_to="medical_reports/"
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.report_name