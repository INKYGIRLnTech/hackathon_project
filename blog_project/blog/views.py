from django.shortcuts import render
from .models import Post



# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {'title': 'About'})

def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post.list.html", {'posts': post_list})
