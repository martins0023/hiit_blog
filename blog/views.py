from django.shortcuts import render


def home(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about-us.html', {'title': 'About'})

def blog(request):
    return render(request, 'blog/blog.html')