from django.forms import ModelForm
from django.contrib.auth.models import User
from signup.models import SignupInfo
from django.forms import SelectDateWidget
import datetime
from django.contrib.auth.forms import UserCreationForm

now = datetime.datetime.now()

class SignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')
		labels = {'email': 'Email'}
		help_texts = {'username': ''}

class SignupForm2(ModelForm):
	class Meta:
		model = SignupInfo
		fields = ['birthdate']
		widgets = {'birthdate': SelectDateWidget(years=range(1900, now.year + 1))}

