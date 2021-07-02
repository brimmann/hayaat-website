from django.urls import path
from django.conf.urls import url

from .views import homePage, readArticle, AboutView


urlpatterns = [
    path('', homePage, name='home'),
    #url(r'^$', HomeView.as_view(), name='home'),
    path('articles/<int:pk>/', readArticle, name='read'),
    path('about/', AboutView.as_view(), name='about')
]