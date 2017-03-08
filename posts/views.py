from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.base import RedirectView

def index(request, username):
	return render(request, 'posts/index.html', {'username': User.objects.get(username=username)})

def archive(request, username=None):
    return render(request, 'posts/archive.html')
	
class UserRedirectView(RedirectView):
	
	def get_redirect_url(self, username):
		return '/%s/posts' % username

