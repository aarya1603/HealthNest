from django import forms
from .models import HealthProfile


class HealthProfileForm(forms.ModelForm):

    class Meta:
        model = HealthProfile

        fields = [
            "full_name",
            "date_of_birth",
            "blood_group",
            "phone",
            "allergies",
            "medical_conditions",
            "emergency_notes",
        ]

        widgets = {

            "date_of_birth": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "allergies": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Example: Penicillin, peanuts..."
                }
            ),

            "medical_conditions": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Example: Diabetes, hypertension..."
                }
            ),

            "emergency_notes": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Anything important doctors or family should know..."
                }
            ),
        }