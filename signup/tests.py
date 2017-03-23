from django.test import TestCase
from django.contrib.auth.models import User
from .models import SignupInfo
import datetime

class SignupTestCase(TestCase):
	def test_one_to_one(self):
		"""verify that SignupInfo is correctly related to a user object via a one-to-one relationship."""
		user = User.objects.create(username="coolperson")
		# chosen date is arbitrary.
		additional_info = SignupInfo.objects.create(user=user, birthdate=datetime.date(month=9, day=25, year=1999))
		user.signupinfo = additional_info
		user.save()
		self.assertEqual(user.signupinfo.user, user)
		self.assertEqual(user.signupinfo.birthdate, datetime.date(month=9, day=25, year=1999))

	
