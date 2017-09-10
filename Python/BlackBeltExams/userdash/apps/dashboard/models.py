from __future__ import unicode_literals
from django.db import models
from ..loginreg.models import User
# Create your models here.
class messageManager(models.Manager):
    def create_message(self, data, owner_id, author):
        owner = User.objects.get(id=owner_id)
        newMessage = Message.objects.create(message=data['message'], author=author, owner=owner)

class commentManager(models.Manager):
    def create_comment(self, data, owner_id, author, message_id):
        owner = User.objects.get(id=owner_id)
        message = Message.objects.get(id=message_id)
        newComment = Comment.objects.create(comment = data['comment'], author=author, owner=owner, message=message)

class Message(models.Model):
    message = models.TextField()
    author = models.ForeignKey(User, related_name='message_author')
    owner = models.ForeignKey(User, related_name = 'message_owner')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = messageManager()

class Comment(models.Model):
    comment = models.TextField()
    message = models.ForeignKey(Message, related_name='comment_message')
    author = models.ForeignKey(User, related_name='comment_author')
    owner = models.ForeignKey(User, related_name='comment_owner')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = commentManager()
