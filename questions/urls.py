from django.urls import path
from .views import QuestionView, send_question


urlpatterns = [
    path('', QuestionView.as_view(), name='ask'),
    path('send_question', send_question, name='send-question'),
]