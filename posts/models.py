from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
        title = models.CharField(max_length=100)
        pub_date = models.DateTimeField('date published', auto_now_add=True)
        body = models.TextField()
        user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, unique=True)

        def utc_to_local(self, utc_datetime):
	        return utc_datetime.astimezone(tz=None)

        def __str__(self):
	        date = self.utc_to_local(self.pub_date).strftime('%m-%d-%y')
	        time = self.utc_to_local(self.pub_date).strftime('%I:%M %p')
	        return '%s at %s \n\n %s \n\n' % (date, time, self.body)


	
