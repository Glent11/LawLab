from django.db import models

class Question(models.Model):
    title = models.CharField('Тема', max_length=50)
    question = models.TextField('Описание')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
