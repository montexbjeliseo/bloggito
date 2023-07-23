from django.db import models
from django.contrib.auth import get_user_model
from apps.posts.models import Post
from django.urls import reverse

class PostComment(models.Model):
    text = models.TextField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now = True, editable=False)
    updated_at = models.DateTimeField(auto_now_add = True, editable=False)
    
    def __str__(self) -> str:
        return f"{self.author.username}: {self.text[:50]}"
    
    def get_delete_url(self):
        return reverse('posts:delete_comment', args=[self.post.pk, self.pk])