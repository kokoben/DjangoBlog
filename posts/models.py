from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	body = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return '%s \n %s \n %s \n\n' % (self.title, str(self.pub_date), self.body)
	
