from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
	username = forms.CharField(max_length=30, required=True,help_text='*(must be between...)')
	first_name = forms.CharField(max_length=30, required=True, help_text='*')
	last_name = forms.CharField(max_length=30, required=False, help_text='')
	email = forms.EmailField(max_length=254, help_text='*')
	password1 = forms.CharField(max_length=30, required=True, help_text='*(must be between...)')
	password2 = forms.CharField(max_length=30, required=True, help_text='*')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )