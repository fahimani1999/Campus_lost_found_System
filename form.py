from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Report


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ReportForm(forms.ModelForm):

    class Meta:
        model = Report

        fields = [
            "item_name",
            "report_type",
            "category",
            "description",
            "location",
            "date",
            "contact_information",
            "image",
        ]

        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date"}
            ),
            "description": forms.Textarea(
                attrs={"rows": 5}
            ),
        }