from django.shortcuts import render
from django.http import HttpResponse

from newsapi import NewsApiClient 
  
# Create your views here.  
def index(request): 
      
    newsapi = NewsApiClient(api_key ='f776a61cf60744cf9f5473701caea44b') 
    top = newsapi.get_top_headlines(sources ='techcrunch') 
  
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[] 
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage']) 
    mylist = zip(news, desc, img) 
  
    return render(request, 'index.html', context ={"mylist":mylist})
