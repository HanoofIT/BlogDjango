

from django.urls import path

from . import views
from .models import post

urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.blogUser, name='users'),
    path('blogs/', views.blogPost, name='posts'),
    path('blogs/details/<int:id>', views.details, name='details'),
    path('category/', views.blogCategories, name='category'),
    path('comments/', views.commPost, name='comments'),

]