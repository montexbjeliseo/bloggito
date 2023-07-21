from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'
    
class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    form_class = PostForm