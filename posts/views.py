from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def index(request, username):
    # if username = None, that means client did not input a username after /posts. this means the client wants to see his own posts page, which he can only do if authenticated. So, check if client is logged in as some user. If he is, render posts page with that user. Otherwise, redirect to login page.
	if username == None:
		if request.user.is_authenticated():
			return redirect('index_with_user', username=request.user.username)
		else:
			return redirect('login')
	else:
		return render(request, 'posts/index.html', {'username': User.objects.get(username=username)})

def archive(request):
    return render(request, 'posts/archive.html')

