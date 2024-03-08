from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

from . import views

urlpatterns = [
    path("", PostListView.as_view(), name="myblog-home"),
    path("user/<str:username>", UserPostListView.as_view(), name="myuser-posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="mypost-detail"),  # blog with the id of post
    path("post/new/", PostCreateView.as_view(), name="mypost-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="mypost-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="mypost-delete"),
    path("about/", views.about, name="myblog-about"),
    
]