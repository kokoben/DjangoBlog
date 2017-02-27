from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
	username = forms.CharField(min_length=1, max_length=150)
	password = forms.CharField(widget=forms.PasswordInput, min_length=1, max_length=100)
