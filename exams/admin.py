from django.contrib import admin
from .models import Exam, Question, Answer

# CustomUser is registered in the `accounts` app admin

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Answer)