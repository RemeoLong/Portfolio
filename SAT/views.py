from django.shortcuts import render


def home(request):
    return render(request, 'index/home.html', {})


def test1(request):
    return render(request, 'index/test1.html', {})


def test2(request):
    return render(request, 'index/test2.html', {})


def test3(request):
    return render(request, 'index/test3.html', {})


def test4(request):
    return render(request, 'index/test4.html', {})


def test5(request):
    return render(request, 'index/test5.html', {})


def test6(request):
    return render(request, 'index/test6.html', {})


def test7(request):
    return render(request, 'index/test7.html', {})


def test8(request):
    return render(request, 'index/test8.html', {})


def final(request):
    return render(request, 'index/final.html', {})


def tips(request):
    return render(request, 'index/tips.html', {})
