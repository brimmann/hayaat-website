from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, TemplateView
from articles.models import Article, Visitor, Bridge

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

    if 'star' in request.GET:
        client_host = request.META['REMOTE_ADDR']
        sta = int(request.GET['star'])
        article_id = int(request.META['PATH_INFO'].replace('/articles/', '').replace('/', ''))

        temp = Visitor.objects.filter(ip__iexact=client_host)
        print(temp)
        if str(temp)=='<QuerySet []>':
            row = Visitor.objects.create(
                ip=client_host,
            )
            client_id = row.pk
        else:
            client_id = temp[0].pk

        temp1 = Bridge.objects.filter(visitor__exact=client_id)
        temp2 = Bridge.objects.filter(article__exact=article_id)
        print(not temp1)
        print(not temp2)

        if not temp1 or not temp2:
            Bridge.objects.create(
                stars=sta,
                visitor=Visitor.objects.get(pk=client_id),
                article=Article.objects.get(pk=article_id),
            )
        else:
            Bridge.objects.filter(visitor__exact=client_id, article__exact=article_id).update(
                stars=sta,
            )

        this_article = Bridge.objects.filter(article__exact=article_id)
        average_stars = 0.0
        i = 0
        for q in this_article:
            average_stars = average_stars + q.stars
            i = i+1

        average_stars = average_stars/i
        Article.objects.filter(id__exact=article_id).update(
            rate = average_stars,
        )
        


    return render(request, 'pages/read_article.html', context)

class AboutView(TemplateView):
    template_name = 'pages/about.html'