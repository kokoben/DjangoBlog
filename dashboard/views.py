from django.shortcuts import render, redirect
from posts.forms import PostForm

def index(request):
    # user has populated the form and is submitting a post. create the post.
    if request.method == "POST":
    	form = PostForm(request.POST)
    	if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('posts:index', username=request.user)
    else:
        form = PostForm
        context = {'form': form}
    return render(request, 'dashboard/index.html', context)
	
