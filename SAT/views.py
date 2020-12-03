from django.http import HttpResponse
from django.template import loader

from .models import Question
from django.shortcuts import render


def home(request):
    return render(request, 'index/home.html', {})


def test1(request):
    return render(request, 'index/test1.html', {})


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


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


def detail(request, question_id):
    return HttpResponse("You're looking at question%s." % question_id)


def result(request, question_id):
    response = "You're looking at the results of question%s."
    return HttpResponse(response % question_id)


