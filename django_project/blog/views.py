from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Post #. means from models in current directory
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "blog/home.html", context)

class PostListView(ListView): # by default, calls posts "object list" instead of post
    model = Post # what model to query to create the list
    template_name = "blog/home.html" # <app>/<model>_<viewtype>.html
    context_object_name = "posts" # what to call the list in the template
    ordering = ["-date_posted"] # order by date_posted

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # current post's author is the currently logged in user
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/" # redirect to home page after deleting post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    #return HttpResponse("<h1>Blog About</h1>")
    return render(request, "blog/about.html", {"title": "About"})

