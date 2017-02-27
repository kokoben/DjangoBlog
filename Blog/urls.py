from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from forms import LoginForm

urlpatterns = [
	url(r'^', include('home.urls')),
	url(r'^signup/', include('signup.urls')),
	url(r'^dash/', include('dashboard.urls')),
	url(r'^posts/', include('posts.urls')),
	url(r'^login/$', auth_views.login, { 'authentication_form': LoginForm}, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page':'login'}, name='logout'),
    url(r'^admin/', admin.site.urls),
]
