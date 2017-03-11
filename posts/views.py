from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.base import RedirectView
from .models import Post
from comments.forms import CommentForm

def index(request, username):
	return render(request, 'posts/index.html', {'username': User.objects.get(username=username)})

def displayPost(request, username, post_number):
	post = Post.objects.get(user=User.objects.get(username=username), id=post_number)

	# display comment form at bottom of post. also handle comment generation.
	if request.method == "POST":
		form = CommentForm(request.POST)
		comment = form.save(commit=False)
		comment.user = request.user
		comment.save()
		
	else:
		form = CommentForm()

	return render(request, 'posts/single_post.html', {'post': post, 'form': form})

def archive(request, username=None):
    return render(request, 'posts/archive.html')
	
class UserRedirectView(RedirectView):
	def get_redirect_url(self, username):
		return '/%s/posts' % username

