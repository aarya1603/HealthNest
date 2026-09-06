from django.db import models
from django.utils import timezone


class Medicine(models.Model):
    """
    Stores basic medicine information
    """

    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)  # e.g. "1 tablet"
    stock = models.PositiveIntegerField()
    low_stock_alert = models.PositiveIntegerField(default=10)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MedicineDose(models.Model):
    """
    Stores WHEN a medicine should be taken (morning/night etc.)
    Allows same medicine multiple times per day
    """

    TIME_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('night', 'Night'),
    ]

    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('alternate', 'Alternate Days'),
    ]

    medicine = models.ForeignKey(
        Medicine,
        on_delete=models.CASCADE
    )

    time_of_day = models.CharField(
        max_length=10,
        choices=TIME_CHOICES
    )

    frequency = models.CharField(
        max_length=10,
        choices=FREQUENCY_CHOICES,
        default='daily'
    )

    def __str__(self):
        return f"{self.medicine.name} - {self.time_of_day}"


class MedicineLog(models.Model):
    """
    Stores taken / skipped status PER DOSE PER DAY
    Prevents double dosing
    """

    STATUS_CHOICES = [
        ('taken', 'Taken'),
        ('skipped', 'Skipped'),
    ]

    medicine_dose = models.ForeignKey(
        MedicineDose,
        on_delete=models.CASCADE
    )

    date = models.DateField(default=timezone.now)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    reason = models.CharField(
        max_length=100,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('medicine_dose', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.medicine_dose} - {self.status} ({self.date})"
