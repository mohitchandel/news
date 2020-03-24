from django.shortcuts import render
from django.http import HttpResponse

from newsapi import NewsApiClient 
  
# Create your views here.  
def index(request): 
      
    newsapi = NewsApiClient(api_key ='f776a61cf60744cf9f5473701caea44b') 
    top = newsapi.get_top_headlines(sources ='techcrunch,ars-technica') 
  
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[]
    link =[]
    published = []
    author = []
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage'])
        link.append(f['url'])
        published.append(f['publishedAt'])
        author.append(f['author'])

    mylist = zip(news, desc, img, link, published, author) 
  
    return render(request, 'index.html', context ={"mylist":mylist})

def world(request): 
      
    newsapi = NewsApiClient(api_key ='f776a61cf60744cf9f5473701caea44b') 
    top = newsapi.get_top_headlines(
    sources ='bbc-news,google-news,vice-news,al-jazeera-english') 
  
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[]
    link =[]
    published = []
    author = []
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage'])
        link.append(f['url'])
        published.append(f['publishedAt'])
        author.append(f['author'])

    mylist = zip(news, desc, img, link, published, author) 
  
    return render(request, 'world.html', context ={"mylist":mylist})

def sports(request): 
      
    newsapi = NewsApiClient(api_key ='f776a61cf60744cf9f5473701caea44b') 
    top = newsapi.get_top_headlines(sources ='espn,talksport,bbc-sport,espn-cric-info') 
  
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[]
    link =[]
    published = []
    author = []
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage'])
        link.append(f['url'])
        published.append(f['publishedAt'])
        author.append(f['author'])

    mylist = zip(news, desc, img, link, published, author) 
  
    return render(request, 'sports.html', context ={"mylist":mylist})


def busin(request): 
      
    newsapi = NewsApiClient(api_key ='f776a61cf60744cf9f5473701caea44b') 
    top = newsapi.get_top_headlines(sources ='business-insider,cnbc,financial-post,fortune') 
  
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[]
    link =[]
    published = []
    author = []
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage'])
        link.append(f['url'])
        published.append(f['publishedAt'])
        author.append(f['author'])

    mylist = zip(news, desc, img, link, published, author) 
  
    return render(request, 'busin.html', context ={"mylist":mylist})


def science(request): 
      
    newsapi = NewsApiClient(api_key ='f776a61cf60744cf9f5473701caea44b') 
    top = newsapi.get_top_headlines(sources ='new-scientist,national-geographic') 
  
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[]
    link =[]
    published = []
    author = []
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage'])
        link.append(f['url'])
        published.append(f['publishedAt'])
        author.append(f['author'])

    mylist = zip(news, desc, img, link, published, author) 
  
    return render(request, 'science.html', context ={"mylist":mylist})


def ente(request): 
      
    newsapi = NewsApiClient(api_key ='f776a61cf60744cf9f5473701caea44b') 
    top = newsapi.get_top_headlines(sources ='buzzfeed,entertainment-weekly,ign,mashable,mtv-news') 
  
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[]
    link =[]
    published = []
    author = []
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage'])
        link.append(f['url'])
        published.append(f['publishedAt'])
        author.append(f['author'])

    mylist = zip(news, desc, img, link, published, author) 
  
    return render(request, 'ente.html', context ={"mylist":mylist})    

