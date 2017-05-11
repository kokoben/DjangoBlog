from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.base import RedirectView
from .models import Post
from comments.models import Comment
from comments.forms import CommentForm
import json

def index(request, username):
    try:
    	User.objects.get(username=username)
    except:
    # user doesn't exist.
    	return render(request, 'posts/index.html', {'username': None})

    return render(request, 'posts/index.html', {'username': User.objects.get(username=username)})

def displayPost(request, username, post_number):
    post = Post.objects.get(user=User.objects.get(username=username), id=post_number)
    comments = Comment.objects.filter(post=post)

    # generate and handle comment form.
    if request.method == "POST":
    	comment_text = request.POST.get('the_comment')

    	comment = Comment(body=comment_text, post=post, user=request.user)
    	comment.save()

    	response_data={'comment': str(comment), 'user':request.user.username, 'comment_count': post.comment_set.count()}
    	
    	return HttpResponse(json.dumps(response_data), content_type='application/json')
		
    else:
    	form = CommentForm()

    return render(request, 'posts/single_post.html', {'post': post, 'comments':comments, 'num_comments':post.comment_set.count(), 'form': form})

def archive(request, username=None):
    return render(request, 'posts/archive.html')

class UserRedirectView(RedirectView):
    def get_redirect_url(self, username):
    	return '/%s/posts' % username

def deletePost(request, username, post_number):
    Post.objects.get(user=User.objects.get(username=username), id=post_number).delete()
    return redirect('posts:index', username=username)

