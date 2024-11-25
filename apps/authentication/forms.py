# forms.py
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "text-white bg-transparent border-b-2 border-gray-300 focus:outline-none focus:border-white",
            }
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "text-white bg-transparent border-b-2 border-gray-300 focus:outline-none focus:border-white",
            }
        )
    )
