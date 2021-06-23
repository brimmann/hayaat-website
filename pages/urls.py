
from django.urls import path

from .views import HomeView, readArticle, AboutView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('articles/', readArticle, name='read'),
    path('about/', AboutView.as_view(), name='about')
]