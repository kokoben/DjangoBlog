from django.shortcuts import render
from posts.forms import PostForm

def index(request):
	form = PostForm
	return render(request, 'dashboard/index.html', {'form':form})
	
