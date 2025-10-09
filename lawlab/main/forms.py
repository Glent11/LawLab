from .models import Question
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
