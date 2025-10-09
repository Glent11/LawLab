from django.shortcuts import render, redirect

from .forms import QuestionForm
from .models import Question


def index(request):
    questions = Question.objects.order_by('-id')
    return render(request, 'main/index.html',
                  {'title': 'Главная страница сайта', 'questions': questions})


def about(request):
    return render(request, 'main/about.html')


def create(request):
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
    return render(request, 'main/create.html', context)
