from django.conf.urls import url
from . import views

app_name = 'comments'

urlpatterns = [
    url(r'^like/(?P<username>\w+)/(?P<post_id>\d+)/$', views.like, name='like'),
    url(r'^reply/(?P<username>\w+)/(?P<comment_id>\d+)/$', views.reply, name='reply')
]

