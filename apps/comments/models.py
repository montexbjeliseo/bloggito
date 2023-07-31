from django.db import models
from django.contrib.auth import get_user_model
from apps.posts.models import Post
from django.urls import reverse

class PostComment(models.Model):
    text = models.TextField(max_length=300, verbose_name='Contenido del comentario')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Articulo al que pertenece')
    author = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, verbose_name='Autor del comentario')
    created_at = models.DateTimeField(auto_now = True, editable=False, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now_add = True, editable=False, verbose_name='Fecha de actualización')
    #editado = models.BooleanField(default=False, verbose_name='Fue editado?')
    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-created_at']
    
    def __str__(self) -> str:
        return f"{self.author.username}: {self.text[:50]}"
    
    def get_delete_url(self):
        return reverse('posts:delete_comment', args=[self.post.pk, self.pk])
    
    def get_update_url(self):
        return reverse('posts:update_comment', args=[self.post.pk, self.pk])