from django.urls import path
from .views import *


app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name = 'index'),
    path('<int:pk>', PostDetailView.as_view(), name = 'view'),
    path('create/', PostCreateView.as_view(), name = 'create'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name = 'delete'),
]
