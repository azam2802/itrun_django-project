from django.db import models
from users.models import *

# Create your models here.
class Posts(models.Model):
    users = models.ForeignKey(User , on_delete= models.CASCADE , related_name='user_post') 
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
 
class PostComment(models.Model):
    users = models.ForeignKey(User , on_delete = models.CASCADE , related_name='user_comment')
    post = models.ForeignKey(Posts , on_delete = models.CASCADE , related_name='post_comment')
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'user {self.users} добавил комментарий в пост {self.post}'

class Meta:
    ordering = ("-created",)