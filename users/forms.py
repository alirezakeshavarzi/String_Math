from django import forms
from .models import User


class LoginForms(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForms(forms.Form):
    username = forms.CharField(max_length=80)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    conf_password = forms.CharField(widget=forms.PasswordInput)
