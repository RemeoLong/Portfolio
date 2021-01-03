from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice, Test, Section
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView


def home(request):
    return render(request, 'index/home.html', {})


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


def tips(request):
    return render(request, 'index/tips.html', {})


class TestList(ListView):
    model = Section
    template_name = 'SAT/test_list.html'
    context_object_name = 'test_list'

    def get_queryset(self):
        return Section.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TestList, self).get_context_data(**kwargs)
        context['TestList'] = Test.objects.all()
        context['Question'] = Question.objects.all()
        return context


def reading(request, test_id, section_id, question_id):
    test = Test.objects.get(Test, pk=test_id)
    section = Section.objects.get(Section, pk=section_id)
    question = Question.objects.get(Question, pk=question_id)
    return render(request, 'index/reading.html', {'question': question})


def writing(request, test_id, section_id):
    return render(request, 'index/writing.html', {})


def mathnc(request, test_id, section_id):
    return render(request, 'index/mathnc.html', {})


def math(request, test_id, section_id):
    return render(request, 'index/math.html', {})


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











