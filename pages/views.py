from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, TemplateView
from django.core.paginator import Paginator
from django.views.decorators.cache import never_cache

from articles.models import Article, Visitor, Bridge

from .templatetags import custome_tags_filters

from .apps import PagesConfig

@never_cache
def homePage(request):
    if 'order' in request.GET:
        if request.GET['order'] == 'visited':
            PagesConfig.current_order = 'visited'
        elif request.GET['order'] == 'rated':
            PagesConfig.current_order = 'rated'
        elif request.GET['order'] == 'dated':
            PagesConfig.current_order = 'dated'
    else:
        if 'page' not in request.GET:
            PagesConfig.current_order = ''
    

    if PagesConfig.current_order == 'visited':
        entire_db = list(Article.objects.order_by('-number_of_visit', 'id'))
        paginator = Paginator(entire_db, 2)
        page = request.GET.get('page')
        query_set = paginator.get_page(page)
        return render(request, 'pages/home.html', {'articles': query_set,})

    elif PagesConfig.current_order == 'rated'  or PagesConfig.current_order == '':
        entire_db = list(Article.objects.order_by('-rate', 'id'))
        paginator = Paginator(entire_db, 2)
        page = request.GET.get('page')
        query_set = paginator.get_page(page)
        return render(request, 'pages/home.html', {'articles': query_set,})

    elif PagesConfig.current_order == 'dated':
        entire_db = list(Article.objects.order_by('-date', 'id'))
        paginator = Paginator(entire_db, 2)
        page = request.GET.get('page')
        query_set = paginator.get_page(page)
        return render(request, 'pages/home.html', {'articles': query_set,})
    
    
    
    
    

    

    
    

def readArticle(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }

    if 'star' in request.GET:
        client_host = request.META['REMOTE_ADDR']
        sta = int(request.GET['star'])
        article_id = int(request.META['PATH_INFO'].replace('/articles/', '').replace('/', ''))
        
        custome_tags_filters.debug_info = "ip: " + client_host
        with open('debug.txt', 'w') as file_object:
            file_object.write("ip: " + client_host)

        temp = Visitor.objects.filter(ip__iexact=client_host)
        
        if not temp:
            row = Visitor.objects.create(
                ip=client_host,
            )
            client_id = row.pk
        else:
            client_id = temp[0].pk

        temp1 = Bridge.objects.filter(visitor__exact=client_id).filter(article__exact=article_id)

        if not temp1:
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
        print(this_article)
        average_stars = 0.0
        i = 0
        for q in this_article:
            average_stars = average_stars + q.stars
            i = i+1
        print('total = ' + str(average_stars))
        average_stars = average_stars/i
        print('average = ' + str(average_stars))
        q = Article.objects.filter(id__exact=article_id)
        Article.objects.filter(id__exact=article_id).update(
            rate = average_stars,
        )
        print(q)
        


    return render(request, 'pages/read_article.html', context)

class AboutView(TemplateView):
    template_name = 'pages/about.html'