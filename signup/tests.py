from django.test import TestCase
from .forms import SignupForm, SignupForm2
import datetime

class SignupTestCase(TestCase):
    ''' verify that newly registered receives additional attributes in SignupInfo.'''
        
    def testSignupBirthdate(self):
        form = SignupForm(data={'username':'tester', 'password1': 'blahblah1', 'password2': 'blahblah1',  'email': 'tester@gmail.com', 'first_name': 'test', 'last_name': 'er'})

        birthdate = datetime.date(month=12, day=22, year=1999)
        form_birth = SignupForm2(data={'birthdate': birthdate})
        if form.is_valid() and form_birth.is_valid():
            new_user = form.save(commit = False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            new_user_birth = form_birth.save(commit=False)
            new_user_birth.user = new_user
            new_user_birth.save()

            self.assertEqual(new_user.signupinfo.birthdate, datetime.date(month=12, day=22, year=1999))
        else:
            print('failed to validate.')
        
