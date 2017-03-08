from django.conf.urls import url
from . import views

app_name= 'posts'

urlpatterns = [
	# posts/ - need to check if user is logged in. if he is, bring to user's posts page. Otherwise, redirect to login page.
	url(r'^$', views.UserRedirectView.as_view(), name='index'),
	url(r'^posts/$', views.index, name='index'),
	url(r'^archive$', views.archive, name='archive')
]

