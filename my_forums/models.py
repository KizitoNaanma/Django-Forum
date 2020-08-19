from django.db import models

# Create your models here.
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
from accounts.models import User

import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/#inclusion-tags
# This is for the in_group_members check template tag
from django import template
register = template.Library()



class Forum(models.Model):
    # name = models.CharField(max_length=255, unique=True)
    topic = models.CharField(blank=True, max_length=100)
    description = models.TextField(blank=True, default='')
    email = models.CharField(blank=True, max_length=100)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description_html = models.TextField(editable=False, default='', blank=True)
    link = models.CharField(blank=True, max_length=100)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    members = models.ManyToManyField(User,through="ForumMember")



    def __str__(self):
        return self.topic

    def save(self, *args, **kwargs):
            self.slug = slugify(self.topic)
            self.description_html = misaka.html(self.description)
            super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("forums:single", kwargs={"slug": self.slug})




class ForumMember(models.Model):
    group = models.ForeignKey(Forum, related_name="memberships",on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_forums',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    # class Meta:
    #     unique_together = ("forum", "user")
