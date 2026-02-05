from .models import Question, Task
from django.forms import ModelForm, TextInput, Textarea


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'question']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оставьте ваш вопрос'}),
            'question': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'})
        }


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название задачи'}),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание задачи'})
        }
