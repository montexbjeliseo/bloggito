from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre de la categoría')
    description = models.TextField(max_length=250, verbose_name='Descripción', null=True)
    created_at = models.DateTimeField(auto_now = True, editable=False, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now_add = True, editable=False, verbose_name='Fecha de actualización')
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def __str__(self) -> str:
        return self.name
    
    def get_filterby_link(self):
        url = reverse('posts:index')
        return f"{url}?category={self.pk}"
    
class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre de la etiqueta')
    description = models.TextField(null=True, verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now = True, editable=False, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now_add = True, editable=False, verbose_name='Fecha de actualización')
    
    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
    
    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título del Artículo')
    short_description = models.TextField(max_length=750, verbose_name='Descripción breve o resumen')
    image = models.ImageField(null=True, verbose_name='Imagen relacionada')
    content = models.TextField(verbose_name='Contenido del artículo')
    created_at = models.DateTimeField(auto_now = True, editable=False, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now_add = True, editable=False, verbose_name='Fecha de actualización')
    author = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, verbose_name='Autor del artículo')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, verbose_name='Categoría a la que pertenece')
    tags = models.ManyToManyField(Tag, verbose_name='Etiquetas relacionadas')
    
    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
    
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
    