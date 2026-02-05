from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('tasks', views.task, name='tasks'),
    path('create_task', views.create_task, name='create_task'),
    path('create_question', views.create_question, name='create_question'),
    path('about', views.about, name='about'),
    path('civil_law', views.civil_law, name='civil_law')
]
