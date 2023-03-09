from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.

def index(request):

    newsapi = NewsApiClient(api_key = "49ae8161878d481aa76cb8a39ecc9a5b")
    top = newsapi.get_top_headlines(sources='techcrunch')

    l = top['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        a = l[i]
        news.append(a['title'])
        desc.append(a['description'])
        img.append(a['urlToImage'])
    newsList = zip(news, desc, img)

    return render(request, 'index.html', context={'newsList': newsList})
