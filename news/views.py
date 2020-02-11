from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
import requests, json, datetime

from .models import News

TOKEN = '4ee7621bf86f4cc7ad34b55089e71e0d'
API_DATA = [{ 'url': 'https://newsapi.org/v2/top-headlines?sources=bbc-news',
'searchUrl' : 'https://newsapi.org/v2/everything',
'headers': { 'Authorization' : 'Basic ' + TOKEN },
'api': 'news'},{ 'url': 'https://reddit.com/r/news/new.json',
'searchUrl': 'https://reddit.com/r/news/search.json', 'headers': {'User-agent': 'bot 0.1'}, 'api': 'reddit'}]

class NewsView(APIView):
    def extractDataFromRedditApi(self, data):
        articles = []
        for posts in data['data']['children']:
            post = {}
            posts = posts['data']
            post['headline'] = posts['title']
            post['link'] = posts['url']
            post['source'] = 'reddit'
            articles.append(post)
        return articles

    def extractDataFromNewsApi(self, data):
        articles = []
        print(data)
        for posts in data['articles']:
            post = {}
            post['headline'] = posts['title']
            post['link'] = posts['url']
            post['source'] = 'newsapi'
            articles.append(post)
        return articles

    def requestNewsApi(self, query = False):
        headers = { 'Authorization' : 'Basic ' + TOKEN }
        if (query):
            url = 'https://newsapi.org/v2/everything'
            r = requests.get(url, headers=headers, params={ 'q' : query })
        else:
            url = 'https://newsapi.org/v2/top-headlines?sources=bbc-news'
            r = requests.get(url, headers=headers)
        responseData = json.loads(r.text)
        return self.extractDataFromNewsApi(responseData)

    def requestRedditApi(self, query = False):
        headers = { 'User-agent': 'bot 0.1' }
        if (query):
            url = 'https://reddit.com/r/news/search.json'
            r = requests.get(url, headers=headers, params={ 'q' : query })
        else:
            url = 'https://reddit.com/r/news/new.json'
            r = requests.get(url, headers=headers)
        responseData = json.loads(r.text)
        return self.extractDataFromRedditApi(responseData)

    def StoreDb(self, articles, query = False):
        for article in articles:
            news=News(query=(query if query else 'list'), request_date=datetime.date.today(),\
                 source=article['source'], headline=article['headline'], link=article['link'])
            news.save()


    def get(self, request):
        query = request.GET.get('query')
        news = []
        if (query):
            news = self.requestNewsApi(query)
            news += self.requestRedditApi(query)
            self.StoreDb(news, query)
        else:
            news = self.requestNewsApi()
            news += self.requestRedditApi()
            self.StoreDb(news)
            
        return Response({"news": news})