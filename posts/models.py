from django.db import models
from django.contrib.auth.models import User

class Archive(models.Model):
	num_posts = models.IntegerField()

class Post(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	page = models.IntegerField(null=True, blank=True)
	body = models.TextField()
	archive = models.ForeignKey(Archive, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	
