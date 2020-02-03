from django.urls import path
from . import views

urlpatterns = [
	path('base', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('', views.index, name="index"),
	path('about', views.about, name = 'about'),
	path('team', views.team, name = 'team'),
	path('blog', views.blog, name = 'blog'),
	path('resources', views.resources, name = 'resources'),
	path('contacts', views.contact, name = 'contact'),
]
