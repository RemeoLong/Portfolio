from django.shortcuts import render


def home(request):
    return render(request, 'index/home.html', {})


def contact(request):
    return render(request, 'index/contact.html', {})


def work(request):
    return render(request, 'index/experience.html', {})


def about(request):
    return render(request, 'index/about.html', {})


def projects(request):
    return render(request, 'index/projects.html', {})