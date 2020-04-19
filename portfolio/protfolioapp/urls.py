from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project', views.project, name='project'),
    path('blog', views.blog, name='blog'),
    path('fullpost', views.fullpost, name='fullpost'),
]