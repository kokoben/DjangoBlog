from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('signup/', include('signup.urls')),
    path('dash/', include('dashboard.urls')),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('<username>/', include('posts.urls')),
    path('comments/', include('comments.urls'))
]

