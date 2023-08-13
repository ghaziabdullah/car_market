from django import forms
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from .models import *


class AdForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"