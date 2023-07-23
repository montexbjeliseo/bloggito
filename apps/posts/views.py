from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from apps.comments.forms import *
from django.shortcuts import redirect

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['postcomment_form'] = PostCommentForm()
        return context
    
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
    
class CommentCreateView(FormView):
    form_class = PostCommentForm
    template_name = 'posts/post_detail.html'

    def form_valid(self, form):
        post_id = self.kwargs['pk']
        post = Post.objects.get(pk=post_id)
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.post = post
        comment.save()

        return super().form_valid(form)
    
    def get_success_url(self):
         return reverse('posts:view', args=[self.kwargs['pk']])