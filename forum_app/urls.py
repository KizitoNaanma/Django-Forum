from django.contrib import admin
from django.urls import path
from forum_app.views import *

urlpatterns = [
    path('',home,name='home'),
    path('addInForum/',addInForum,name='addInForum'),
    path('addInDiscussion/',addInDiscussion,name='addInDiscussion'),
]
