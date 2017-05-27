from django.forms import ModelForm
from .models import Comment, Reply
from django import forms

class CommentForm(ModelForm):
    class Meta:	
    	model = Comment
    	fields = ('body',)
    	widgets = {'body': forms.Textarea(attrs={'id': 'comment-text'})}

class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ('body',)
        widgets = {'body': forms.Textarea(attrs={'id': 'reply-text'})}
