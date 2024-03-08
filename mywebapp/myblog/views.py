from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post



def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, 'myblog/home.html', context=context)

# These are class based views
class PostListView(ListView):
    model = Post
    template_name = "myblog/home.html" #<app>/<model>_<viewtype>.html
    context_object_name = "posts" # PostListView will be referenced as posts in html, because in the mentioned as posts in the context 
    ordering = ['-date_posted'] # Post newest to oldest
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = "myblog/user_posts.html"
    context_object_name = "posts" 
    paginate_by = 5
    
    def get_queryset(self) -> QuerySet[Any]:
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self, form) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self, form) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"
    
    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def about(request):
    return render(request, "myblog/about.html", {"title": "about"})