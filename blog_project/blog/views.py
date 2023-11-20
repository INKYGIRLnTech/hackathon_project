from django.shortcuts import render
from .models import Post



# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/home.html", context)

def article(request):
    return render(request, "blog/article.html", {})

def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post.list.html", {'posts': post_list})
