from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def index(request, username):
	# if username = None, that means client did not input a username after /posts. this means the client wants to see his own posts page, which he can only do if authenticated. So, check if client is logged in as some user. If he is, render posts page with that user. Otherwise, redirect to login page.
	if username == None:
		if request.user.is_authenticated():
			return HttpResponseRedirect(reverse('index_with_user', kwargs={'username':request.user.username}))
		else:
			return HttpResponseRedirect(reverse('login'))
	else:
		return render(request, 'posts/index.html', {'username': User.objects.get(username=username)})

def archive(request):
	return render(request, 'posts/archive.html')

