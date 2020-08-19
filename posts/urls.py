from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path("post/in/(?P[-\w]+)/",views.SinglePost.as_view(),name="single"),
    path("new/",views.CreatePost.as_view(),name="create"),
    path("list/",views.ListPosts.as_view(),name="list")
]
