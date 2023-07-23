from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect

class AuthLoginView(UserPassesTestMixin, LoginView):
    template_name='auth/login.html'
    login_url = reverse_lazy('login')
    
    def test_func(self):
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self):
        
        return redirect(f"{reverse_lazy('confirm_logout')}?next={self.login_url}")
    
class AuthConfirmLogoutView(LoginView):
    template_name = 'auth/confirm_logout.html'