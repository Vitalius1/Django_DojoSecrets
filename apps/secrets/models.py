from __future__ import unicode_literals

from django.db import models
from ..login_registration.models import User
from django.db.models import Count

class SecretManager(models.Manager):
    def create_secret(self, postData, user_id):
        secret = self.create(content = postData['the_secret'], creator = User.objects.get(id = user_id))
        return secret

    def add_like(self, postData):
        the_user = User.objects.get(id = postData['user_id'])
        the_secret = Secret.objects.get(id = postData['secret_id'])
        the_secret.like.add(the_user)
        likes_count = Secret.objects.annotate(num_likes = Count('like'))
        return likes_count

class Secret(models.Model):
    content = models.TextField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    creator = models.ForeignKey(User, related_name = "creator", null = True)
    like = models.ManyToManyField(User, related_name = "liked")

    objects = SecretManager()

# Create your models here.
