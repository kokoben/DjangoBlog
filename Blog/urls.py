from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^', include('home.urls')),
	url(r'^signup/', include('signup.urls')),
	url(r'^dash/', include('dashboard.urls')),
	url(r'^login/$', views.custom_login, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page':'login'}, name='logout'),
    url(r'^admin/', admin.site.urls),
	url(r'^(?P<username>\w+)/', include('posts.urls')),
        url(r'^comments/', include('comments.urls'))

]

