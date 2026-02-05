from django.shortcuts import render, redirect

from .forms import QuestionForm, TaskForm
from .models import Question, Task, CourtDecision


def index(request):
    questions = Question.objects.order_by('-id')
    return render(request, 'main/index.html',
                  {'title': 'Главная страница сайта', 'questions': questions})


def task(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/tasks.html',
                  {'title': 'Задачи', 'tasks': tasks})


def create_task(request):
    err = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else:
            err = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': err
    }
    return render(request, 'main/create_task.html', context)



def about(request):
    return render(request, 'main/about.html')


def create_question(request):
    err = ''
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            err = 'Форма была неверной'

    form = QuestionForm()
    context = {
        'form': form,
        'error': err
    }
    return render(request, 'main/create_question.html', context)


def civil_law(request):
    court_decisions = CourtDecision.objects.order_by('-id')
    return render(request, 'main/civil_law.html',
                  {'title': 'Гражданское право', 'court_decisions': court_decisions})
