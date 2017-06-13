from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.base import RedirectView
from .models import Post
from comments.models import Comment, Reply
from comments.forms import CommentForm, ReplyForm

def index(request, username):
    try:
    	User.objects.get(username=username)
    except:
        # user doesn't exist.
        context = {'username': None}
        return render(request, 'posts/index.html', context)

    user = User.objects.get(username=username)
    context = {'username': user}
    return render(request, 'posts/index.html', context)

def displayPost(request, username, post_number):
    post = Post.objects.get(user=User.objects.get(username=username), id=post_number)
    comments = Comment.objects.filter(post=post)

    # generate or handle comment form.
    if request.method == "POST":
        comment_text = request.POST.get('the_comment')
        comment = Comment(body=comment_text, post=post, user=request.user)
        comment.save()
        user = request.user.username
        num_comments = post.comment_set.count()
        response_data = {
        'comment': str(comment), 
        'comment_id': comment.id,
        'user':user,
        'comment_count': num_comments
        }
        return JsonResponse(response_data)
    else:
        comment_form = CommentForm()
        reply_form = ReplyForm()

    num_comments = post.comment_set.count()
    context = {
        'post': post,
        'comments':comments,
        'num_comments':num_comments,
        'comment_form': comment_form,
        'reply_form': reply_form # not initially in template. generated via ajax call if user clicks on reply link.
    }
    return render(request, 'posts/single_post.html', context)

def handleReply(request, username, comment_number):
# username is of the posts's user.
    comment = Comment.objects.get(user=User.objects.get(username=username), id=comment_number)
    if request.method == "POST":
        reply_text = request.POST.get('the_reply')
        reply = Reply(body=reply_text, comment=comment, user=request.user)
        reply.save()
        user = request.user.username
        response_data = {
            'reply': str(reply),
            'user': user,
        }
        return JsonResponse(response_data)

def archive(request, username=None):
    return render(request, 'posts/archive.html')

class UserRedirectView(RedirectView):
    def get_redirect_url(self, username):
    	return '/%s/posts' % username

def deletePost(request, username, post_number):
    Post.objects.get(user=User.objects.get(username=username), id=post_number).delete()
    return redirect('posts:index', username=username)

