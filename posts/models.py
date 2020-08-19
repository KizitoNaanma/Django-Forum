from django.db import models

# Create your models here.

from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
from accounts.models import User
from my_forums.models import Forum
import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/#inclusion-tags
# This is for the in_group_members check template tag
from django import template
register = template.Library()



class Discussion(models.Model):
    forum = models.ForeignKey(Forum, related_name="posts",null=True, blank=True,on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)
    user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)

    def __str__(self):
        return str(self.message)


    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "forums:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "message"]
