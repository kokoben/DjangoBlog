from django.shortcuts import render
from posts.forms import PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
	# user has populated the form and is submitting a post. create the post.
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.user = request.user
			new_post.save()
			# redirect user to posts page.
			return HttpResponseRedirect(reverse('posts:index'))
	else:
		form = PostForm
	return render(request, 'dashboard/index.html', {'form':form})
	
