from django.db import models


RELATIONSHIP_CHOICES = [
    ("Mother", "Mother"),
    ("Father", "Father"),
    ("Brother", "Brother"),
    ("Sister", "Sister"),
    ("Spouse", "Spouse"),
    ("Son", "Son"),
    ("Daughter", "Daughter"),
    ("Friend", "Friend"),
    ("Caregiver", "Caregiver"),
    ("Other", "Other"),
]


class EmergencyContact(models.Model):

    name = models.CharField(
        max_length=100
    )

    relationship = models.CharField(
        max_length=50,
        choices=RELATIONSHIP_CHOICES
    )

    phone = models.CharField(
        max_length=20
    )

    def __str__(self):
        return f"{self.name} ({self.relationship})"