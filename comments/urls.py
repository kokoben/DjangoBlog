from django.conf.urls import url
from . import views

app_name = 'comments'

urlpatterns = [
    url(r'^like/(?P<username>\w+)/(?P<post>\d+)/$', views.like, name='like')
]

