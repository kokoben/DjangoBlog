from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.base import RedirectView
from .models import Post
from comments.models import Comment
from comments.forms import CommentForm

def index(request, username):
	return render(request, 'posts/index.html', {'username': User.objects.get(username=username)})

def displayPost(request, username, post_number):
	post = Post.objects.get(user=User.objects.get(username=username), id=post_number)
	comments = Comment.objects.filter(post=post)

	# generate and handle comment form.
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = request.user
			comment.post = post
			comment.save()
			return redirect('posts:display-post', username=username, post_number=post_number)
		
	else:
		form = CommentForm()

	return render(request, 'posts/single_post.html', {'post': post, 'comments':comments, 'form': form})

def archive(request, username=None):
    return render(request, 'posts/archive.html')
	
class UserRedirectView(RedirectView):
	def get_redirect_url(self, username):
		return '/%s/posts' % username

