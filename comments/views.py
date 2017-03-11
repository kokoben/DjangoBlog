from django.shortcuts import render
from .forms import CommentForm
from django.shortcuts import redirect

def displayCommentForm(request, post_username):
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.save()
            # return user to posts page of the user whose post was being commented on.
            return redirect('posts:index', username=post_username)
    else:
        form = CommentForm()
		

