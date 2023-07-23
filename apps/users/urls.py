from django.urls import path
from .views import *

urlpatterns = [
    path('login/', AuthLoginView.as_view(), name = 'login'),    
    path('logout/', AuthLogoutView.as_view(), name = 'logout'),  
    path('confirm_logout', AuthConfirmLogoutView.as_view(), {'next_page': None}, name = 'confirm_logout'),
    path('register/', AuthRegisterUserView.as_view(), {'next_page': None}, name = 'register'),  
]
