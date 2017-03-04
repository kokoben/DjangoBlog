from django.conf.urls import url
from . import views

app_name= 'posts'

urlpatterns = [
	# posts/ - need to check if user is logged in. if he is, bring to user's posts page. Otherwise, redirect to login page.
	url(r'^$', views.index, {'username': None }, name='index'),
	# posts/(username)/ - client is requesting posts page of specific user. bring client to that user's posts page.
	url(r'^(?P<username>\w+)/$', views.index),
	url(r'^archive$', views.archive, name='archive')
]

