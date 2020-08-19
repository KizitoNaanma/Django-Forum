from django.urls import path
from . import views

app_name = 'my_forums'

urlpatterns = [
    path("", views.ListForums.as_view(), name="all"),
    path("new/", views.CreateForum.as_view(), name="create"),
    path("posts/in/(?P<slug>[-\w]+)/",views.SingleForum.as_view(),name="single"),

]
