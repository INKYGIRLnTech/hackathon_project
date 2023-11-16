from django.shortcuts import render

posts = [
    {
        'Author': 'UserOne',
        'Title': 'Blog Post 1',
        'Content': 'First post content',
        'Genre': 'Hip-hop',
        'Date_posted': 'November 16, 2023'
    },
    {
        'Author': 'UserTwo',
        'Title': 'Blog Post 2',
        'Content': 'Second post content',
        'Genre': 'R&B',
        'Date_posted': 'November 17, 2023'
    },
    {
        'Author': 'UserThree',
        'Title': 'Blog Post 3',
        'Content': 'Third post content',
        'Genre': 'Pop',
        'Date_posted': 'October 31, 2023'
    }
]

# Create your views here.

def home(request):
    context = {
        'posts': posts
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {'title': 'About'})

