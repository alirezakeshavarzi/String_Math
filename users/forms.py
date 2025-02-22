from django import forms
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm

from .models import User



class LoginForms(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForms(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdatePersonalInfoForms(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']