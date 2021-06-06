from os import name
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import re_path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('add', views.add,name='Add'),
    path('addposts', views.AddPostView.as_view(), name='AddPost'),
    path('addvideo', views.AddVideoView.as_view(), name='AddVideo'),
    path('users/', views.UserView.as_view(), name='UserView'),
    path('search/', views.Search.as_view(), name='Search'),
    path('users/<str:pk>/', views.UserDetail.as_view(), name='UserDetail'),
    path('post/<int:pk>/', views.PostView.as_view(), name='PostView'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='PostUpdate'),
    path('post/<int:pk>/videoupdate/', views.VideoUpdate.as_view(), name='VideoUpdate'),
    path('post/<int:pk>/delete/', views.PostDel.as_view(), name='PostDelete'),  
    path('404/', views.Page404, name='404'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
