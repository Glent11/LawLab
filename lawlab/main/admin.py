from django.contrib import admin
from .models import Question, Task, CourtDecision


admin.site.register(Question)
admin.site.register(Task)
admin.site.register(CourtDecision)
