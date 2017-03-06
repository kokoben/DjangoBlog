from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	body = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def utc_to_local(self, utc_datetime):
		return utc_datetime.astimezone(tz=None)

	def __str__(self):
		date_time = self.utc_to_local(self.pub_date).strftime('%m-%d-%y %I:%M %p')
		return '%s \n %s \n %s \n\n' % (self.title, date_time , self.body)
	
