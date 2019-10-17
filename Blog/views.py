from django.contrib.auth import login
from django.shortcuts import redirect

def custom_login(request):
	""" wrapper of django's login view that redirects user to dash if user is already logged in and tries to access the login page via its url."""
	if request.user.is_authenticated:
		return redirect('dashboard:index')
	else:
		return login(request)
