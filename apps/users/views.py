from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, TemplateView
from django.contrib.auth import get_user_model, login
from .forms import *
from .models import *


class AuthLoginView(UserPassesTestMixin, LoginView):
    template_name = "auth/login.html"
    login_url = reverse_lazy("login")

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect(f"{reverse_lazy('confirm_logout')}?next={self.login_url}")

class AuthConfirmLogoutView(UserPassesTestMixin, TemplateView):
    template_name = "auth/confirm_logout.html"
    
    def test_func(self):
        return self.request.user.is_authenticated
    
    def handle_no_permission(self):
        return redirect(reverse_lazy("login"))


class AuthRegisterUserView(UserPassesTestMixin, CreateView):
    model = get_user_model()
    template_name = "auth/register.html"
    form_class = UserForm
    success_url = reverse_lazy("index")

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        confirm_logout_url = reverse_lazy("confirm_logout")
        next_page = reverse_lazy("register")
        return redirect(f"{confirm_logout_url}?next={next_page}")

    def get_success_url(self) -> str:
        success_url = super().get_success_url()
        next_page = self.request.GET.get("next")
        if next_page:
            success_url = next_page
        return success_url

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class AuthLogoutView(UserPassesTestMixin, LogoutView):
    template_name = 'auth/logout.html'
    success_url = reverse_lazy('login')
    
    def get_success_url(self) -> str:
        success_url = super().get_success_url()
        next_page = self.request.GET.get("next")
        if next_page:
            success_url = next_page
        return success_url
    
    def test_func(self):
        return self.request.user.is_authenticated
    
    def handle_no_permission(self):
        return redirect(reverse_lazy("login"))
    
class UserProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'user_data'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    