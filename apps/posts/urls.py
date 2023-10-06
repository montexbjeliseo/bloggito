from django.urls import path
from .views import *


app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name = 'index'),
    path('<int:pk>', PostDetailView.as_view(), name = 'view'),
    path('create/', PostCreateView.as_view(), name = 'create'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name = 'delete'),
    path('<int:pk>/update', PostUpdateView.as_view(), name = 'update'),
    path('<int:pk>/like', like_post, name = 'like'),
    path('<int:pk>/comment', PostCommentCreateView.as_view(), name = 'add_comment'),
    path('<int:pk>/comment/<int:cpk>/delete', PostCommentDeleteView.as_view(), name = 'delete_comment'),
    path('<int:pk>/comment/<int:cpk>/update', PostCommentUpdateView.as_view(), name = 'update_comment'),
    path('category/create', PostCategoryCreateView.as_view(), name = 'create_category'),
    path('category/<int:pk>/update', PostCategoryUpdateView.as_view(), name = 'update_category'),
    path('category/<int:pk>/delete', PostCategoryDeleteView.as_view(), name = 'delete_category'),
]
