from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import ArticleAbout


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def about_article(request, pk):
    article = get_object_or_404(ArticleAbout, pk=pk)
    return render(request, 'about.html', {'article': article})


def commemoration(request):
    return render(request, 'commemoration.html')


def contacts(request):
    return render(request, 'contacts.html')


def events(request):
    return render(request, 'events.html')


def events_article(request):
    article = get_object_or_404(ArticleAbout, pk=pk)
    return render(request, 'events.html', {'article': article})


def schedule(request):
    return render(request, 'schedule.html')
