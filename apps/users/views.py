from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth import get_user_model, login
from .forms import *


class AuthLoginView(UserPassesTestMixin, LoginView):
    template_name = "auth/login.html"
    login_url = reverse_lazy("login")

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect(f"{reverse_lazy('confirm_logout')}?next={self.login_url}")


class AuthConfirmLogoutView(LoginView):
    template_name = "auth/confirm_logout.html"


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
