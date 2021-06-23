from django.urls import path
from .views import QuestionView


urlpatterns = [
    path('', QuestionView.as_view(), name='ask'),
]