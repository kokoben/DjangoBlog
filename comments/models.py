from django.db import models
from posts.models import Post

class Comment(models.Model):
	body = models.TextField()
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	comment_number = models.IntegerField()
