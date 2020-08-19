from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic

from posts.models import Discussion


class CreatePost(LoginRequiredMixin,generic.CreateView):
    fields = ('discuss')
    model = Discussion

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class SinglePost(generic.DetailView):
    model = Discussion
    select_related = ("user", "forum")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )


class ListPosts(generic.ListView):
    model = Discussion
    select_related = ("user", "forum")
