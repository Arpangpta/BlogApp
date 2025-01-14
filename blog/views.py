from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted' :'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

# Create your views here.

def home(request):

    context = {
        'posts': posts
        }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})

def base(request):
    return render(request, 'blog/base.html',{'title':'Base'})