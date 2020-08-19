from django.shortcuts import render
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic

from my_forums.models import Forum


class CreateForum(LoginRequiredMixin,generic.CreateView):
    fields = ('topic','description','email','link')
    model = Forum

class SingleForum(generic.DetailView):
    model = Forum

class ListForums(generic.ListView):
    model = Forum
