from django.urls import path, include
from . import views

app_name='signup'

urlpatterns = [
	path('', views.index, name="index"),
	path('success/', views.success, name="success")
]

