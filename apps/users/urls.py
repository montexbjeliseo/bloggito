from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('login/', AuthLoginView.as_view(), name = 'login'),    
    path('logout/', LogoutView.as_view(), name = 'logout'),  
    path('confirm_logout', AuthConfirmLogoutView.as_view(), {'next_page': None}, name = 'confirm_logout')  
]
