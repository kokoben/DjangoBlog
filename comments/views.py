from posts.models import Post
from django.http import JsonResponse
from django.contrib.auth.models import User

def like(request, username, post_id):
    '''handles ajax response for when user clicks a post's like button.'''
    post = Post.objects.get(user=User.objects.get(username=username), id=post_id)

    if post.like_set.filter(liker=request.user).exists():
    	# user has already liked this post, so unlike it.
    	post.like_set.get(post=post, liker=request.user).delete()
        # flag indicating that the post was liked before function call.
    	liked = True
    else:
    	# user has not yet liked the post, so like it.
    	post.like_set.create(post=post, liker=request.user)
        # flag indicating that the post was unliked before function call.
    	liked = False

    # need post id to target the correct post's likes count in the ajax response using the html id attribute.
    response_data = {
        'liked': liked,
        'likes_count': post.like_set.count(),
        'post_id': post.id
    }
    return JsonResponse(response_data)

def reply(request, username, post_id, comment_id):
    '''handles ajax response for when user replies to a comment.'''
    
    post = Post.objects.get(id=post_id)
    comments = post.comment_set.all().values('id')
    comments_list = list(comments)
    response_data = {
        'username': username,
        'comment_id': comment_id,
        'comments_list': comments_list,
        'num_comments': post.comment_set.count() 
    }
    return JsonResponse(response_data)
