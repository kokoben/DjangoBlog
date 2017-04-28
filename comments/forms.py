from django.forms import ModelForm
from .models import Comment
from django import forms

class CommentForm(ModelForm):
	class Meta:	
		model = Comment
		fields = ('body',)
		widgets = {'body': forms.Textarea(attrs={'id': 'comment-text'})}
