from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    FormView,
)
from .models import *
from .forms import *
from django.urls import reverse_lazy
from apps.comments.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["postcomment_form"] = PostCommentForm()
        return context


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    template_name = "posts/post_create.html"
    form_class = PostForm

    def test_func(self):
        return self.request.user.is_staff


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = reverse_lazy("posts:index")

    def test_func(self):
        return self.request.user.is_staff


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    success_url = reverse_lazy("posts:index")
    form_class = PostForm

    def test_func(self):
        return self.request.user.is_staff


class PostCommentCreateView(LoginRequiredMixin, FormView):
    form_class = PostCommentForm
    template_name = "posts/post_detail.html"

    def form_valid(self, form):
        post_id = self.kwargs["pk"]
        post = Post.objects.get(pk=post_id)
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.post = post
        comment.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("posts:view", args=[self.kwargs["pk"]])


class PostCommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostComment
    template_name = "posts/comments/delete.html"
    pk_url_kwarg = "cpk"

    def get_success_url(self):
        return reverse("posts:view", args=[self.kwargs["pk"]])

    def test_func(self):
        cpk = self.kwargs["cpk"]
        comment = PostComment.objects.get(pk=cpk)
        return self.request.user == comment.author or self.request.user.is_staff


class PostCommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostComment
    template_name = "posts/comments/update.html"
    form_class = PostCommentForm
    pk_url_kwarg = "cpk"

    def get_success_url(self):
        return reverse("posts:view", args=[self.kwargs["pk"]])

    def test_func(self):
        cpk = self.kwargs["cpk"]
        comment = PostComment.objects.get(pk=cpk)
        return self.request.user == comment.author
