from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from articles.models import Article

class HomeView(ListView):
    model = Article
    paginate_by = 5
    template_name = 'pages/home.html'
    context_object_name = 'articles'
    
    
    

def readArticle(request):
    return render(request, 'pages/read_article.html')

class AboutView(TemplateView):
    template_name = 'pages/about.html'