from django.urls import path,include

from facenet import views

urlpatterns = [
	path('hello_world', views.hello_world, name='hello_world'),
]
