from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now = True, editable=False)
    updated_at = models.DateTimeField(auto_now_add = True, editable=False)
    
    def __str__(self) -> str:
        return self.name
    
    def get_filterby_link(self):
        url = reverse('posts:index')
        return f"{url}?category={self.pk}"
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now = True, editable=False)
    updated_at = models.DateTimeField(auto_now_add = True, editable=False)
    
    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    image = models.ImageField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)
    author = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('posts:view', args=[self.pk])
    
    def get_delete_url(self):
        return reverse('posts:delete', args=[self.pk])
    
    def get_update_url(self):
        return reverse('posts:update', args=[self.pk])
    
    def get_add_comment_url(self):
        return reverse('posts:add_comment', args=[self.pk])
    