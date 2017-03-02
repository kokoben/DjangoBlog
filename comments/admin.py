from django.contrib import admin
from django.forms import ModelForm
from .models import Comment

class ArticleForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['body']


