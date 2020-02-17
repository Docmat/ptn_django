
from django.urls import path
from .import views


urlpatterns = [
    path('posts/', views.main_page, name="main-page"),
    path('posts/<int:pk>/', views.post_detail, name="post-detail"),
    path('posts/create/', views.post_create, name="post-create")
]
