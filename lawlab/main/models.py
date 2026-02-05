from django.db import models


class Question(models.Model):
    title = models.CharField('Тема', max_length=50)
    question = models.TextField('Описание')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Task(models.Model):
    title = models.CharField('Тема', max_length=50)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class CourtDecision(models.Model):
    uid = 0
    case_number = 0
    date = models.DateField('Дата')
    court_name = ''
    somefield1 = ''
    # somefield2 = models.
    title = models.TextField('Шапка')
    body = models.TextField('Тело')
    decision = models.TextField('Решение')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Судебное решение'
        verbose_name_plural = 'Судебные решения'
