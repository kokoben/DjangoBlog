from django.db import models
from posts.models import Post
from django.contrib.auth.models import User

class Comment(models.Model):
	body = models.TextField()
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def utc_to_local(self, utc_datetime):
		return utc_datetime.astimezone(tz=None)

	def __str__(self):
		date = self.utc_to_local(self.pub_date).strftime('%m-%d-%y')
		time = self.utc_to_local(self.pub_date).strftime('%I:%M %p')
		return '%s at %s \n %s \n' % (date, time, self.body)
