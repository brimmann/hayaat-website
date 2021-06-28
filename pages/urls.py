
from django.urls import path
from django.conf.urls import url

from .views import HomeView, readArticle, AboutView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    #url(r'^$', HomeView.as_view(), name='home'),
    path('articles/', readArticle, name='read'),
    path('about/', AboutView.as_view(), name='about')
]