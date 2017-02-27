from django.shortcuts import render

def index(request):
	return render(request, 'posts/index.html')
	

def archive(request):
	return render(request, 'posts/archive.html')

