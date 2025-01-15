from django.shortcuts import render
from django.http import HttpResponse
from .models import Post #. means from models in current directory

def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "blog/home.html", context)

def about(request):
    #return HttpResponse("<h1>Blog About</h1>")
    return render(request, "blog/about.html", {"title": "About"})
