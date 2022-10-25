from re import U
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.home, name='home'),
    path("post/", views.post, name='post'),
    path("author/", views.author, name='author'),
]