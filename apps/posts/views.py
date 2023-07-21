from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView
from .models import *
from .forms import *
from django.urls import reverse_lazy

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
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('posts:index')
    
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_update.html'
    success_url = reverse_lazy('posts:index')
    form_class = PostForm
    
class FakeLogin(FormView):
    template_name = 'posts/fake_login.html'
    
    def get_success_url(self) -> str:
        next_url = ''
        #next_url = self.request.POST["next"]
        
        return next_url
        
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        next_url = ''
        ctx = super().get_context_data(**kwargs)
        # if self.request.method == "GET":
        #     if "next" in self.request.GET:
        #         next_url = self.request.GET["next"]
        # ctx["next"] = next_url
        return ctx