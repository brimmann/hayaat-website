from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, TemplateView
from articles.models import Article

class HomeView(ListView):
    model = Article
    ordering = ['number_of_visit']
    print("CALLED")
    paginate_by = 5
    template_name = 'pages/home.html'
    context_object_name = 'articles'

    def get_queryset(self):
        if 'order' in self.request.GET:
            if self.request.GET['order'] == 'visited':
                print("PRINTED")
                return Article.objects.order_by('-number_of_visit')
            elif self.request.GET['order'] == 'rated':
                return Article.objects.order_by('-rate')
            elif self.request.GET['order'] == 'dated':
                return Article.objects.order_by('-date')
        else:
            return Article.objects.order_by('-number_of_visit')
    
    
    

def readArticle(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'pages/read_article.html', context)

class AboutView(TemplateView):
    template_name = 'pages/about.html'