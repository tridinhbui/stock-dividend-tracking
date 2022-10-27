from django.shortcuts import render

posts = [
    {
        'author': 'Tri ',
        'title': 'Blog Post 1',
    },
    {
        'author': 'Bui ',
        'title': 'Blog Post 2',
    }
]


def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'stock/home.html', context)


def usStock(request):
    return render(request, 'stock/usStock.html')
