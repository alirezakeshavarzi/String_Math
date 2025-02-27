from django import forms
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm, PasswordChangeForm

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

from django.contrib.auth.forms import PasswordChangeForm
from django import forms

class UpdatePassword(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


# class UpdatePassword(PasswordChangeForm):
#     old_password = forms.CharField(
#         label="Current Password",
#         widget=forms.PasswordInput(attrs={'name': 'Current_Password'})
#     )
#     new_password1 = forms.CharField(
#         label="New Password",
#         widget=forms.PasswordInput(attrs={'name': 'New_Password'})
#     )
#     new_password2 = forms.CharField(
#         label="Confirm New Password",
#         widget=forms.PasswordInput(attrs={'name': 'Confirm_New_Password'})
#     )
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['old_password'].widget.attrs['name'] = 'Current_Password'
#         self.fields['new_password1'].widget.attrs['name'] = 'New_Password'
#         self.fields['new_password2'].widget.attrs['name'] = 'Confirm_New_Password'
#
#     class Meta:
#         model = User
#         fields = ['Current_Password', 'New_Password', 'Confirm_New_Password']