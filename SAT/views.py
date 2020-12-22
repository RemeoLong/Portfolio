from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice, Passage, Explanation, Test, Section
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


def home(request):
    return render(request, 'index/home.html', {})


def tips(request):
    return render(request, 'index/tips.html', {})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://remeolong.pythonanywhere.com/SAT/home')
    else:
        form = UserCreationForm()
    return render(request, 'index/register.html', {'form': form})


def test(request):
    return render(request, 'index/test.html', {})


def section(request, test_id):
    return render(request, 'index/section.html', {})


def quiz(request, test_id):
    try:
        test = Test.objects.get(pk=test_id)
    except Test.DoesNotExist:
        raise Http404("Sorry, Test does not exist")
    return render(request, 'index/quiz.html', {'test': test})


def sect(request, test_id, section_id):
    try:
        section = Section.objects.get(pk=section_id)
    except Section.DoesNotExist:
        raise Http404("Sorry, There is no Section with that name. ")
    return render(request, 'index/sect.html', {'section': section})


def detail(request, test_id, section_id, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Sorry, Question does not exist")
    return render(request, 'index/details.html', {'question': question})


def result(request, test_id, section_id, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice = question.choice_set.all().first()
    context = {'question': question, 'choice': choice}
    return render(request, 'index/results.html', context)


def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_answer = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'index/details.html', {
            'question': question,
            'error_message': "A Choice was not selected. Please make a selection.",
        })
    else:
        selected_answer.answer = selected_answer.choice_text
        selected_answer.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))


def final(request):
    return render(request, 'index/final.html', {})
