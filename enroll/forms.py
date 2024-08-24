from django import forms
from .models import User
from django.core import validators

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name","address","email","password"]
        widgets = {
            "name": forms.TextInput(attrs={'class':'form-control'}),
            "address": forms.TextInput(attrs={'class':'form-control'}),
            "email": forms.TextInput(attrs={'class':'form-control'}),
            "password": forms.PasswordInput(render_value=True , attrs={'class':'form-control'}),

        }