from django.shortcuts import render

from .models import Line, Post

def home(request):
    data = Post.objects.all()
    datal = Line.objects.all()
    return render(request, 'home.html', {'posts': data, 'lines':datal})

def index(request):
    data = Post.objects.all()
    datal = Line.objects.all()
    return render(request, 'index.html', {'posts': data, 'lines':datal})

def single(request, slug):
    data = Post.objects.get(slug=slug)
    return render(request, 'single.html',{'post': data})


def about(request):
    return render(request, 'about.html', {})

def Direktor(request):
    return render(request, 'direktor.html', {})

def Rahbariyat(request):
    return render(request, 'Rahbariyat.html', {})

def IT_ticher(request):
    return render(request, 'IT_ticher.html', {})