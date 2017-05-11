from posts.models import Post
from django.http import HttpResponse
from django.contrib.auth.models import User
import json

def like(request, username, post):
    "handles ajax response for when user clicks a post's like button."
    post = Post.objects.get(user=User.objects.get(username=username), id=post)

    if post.like_set.filter(liker=request.user).exists():
    	# user has already liked this post, so unlike it.
    	post.like_set.get(post=post, liker=request.user).delete()
    	# decrease number of total likes for the post.
    	liked = True
    else:
    	# user has not yet liked the post, so like it.
    	post.like_set.create(post=post, liker=request.user)
    	# increase number of total likes for the post.
    	liked = False

    # need post id to target the correct post's likes count in the ajax response using the html id attribute.
    response_data = {'liked': liked, 'likes_count': post.like_set.count(), 'post_id': post.id}

    return HttpResponse(json.dumps(response_data), content_type='application/json')
