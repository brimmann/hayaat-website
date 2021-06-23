from django.shortcuts import render
from django.views.generic import TemplateView

class QuestionView(TemplateView):
    template_name = 'questions/ask_question.html'
    print(template_name)
