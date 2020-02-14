from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework import status
import requests, json, datetime
from .serializers import NewsSerializer
from .models import News

#Should be stored as an environment variable
TOKEN = '4ee7621bf86f4cc7ad34b55089e71e0d'

@api_view(['GET', ])
class NewsView(ListAPIView):
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

    def storeInDb(self, articles, query = False):
        for article in articles:
            news=News(query=(query if query else 'list'), request_date=datetime.date.today(),\
                 source=article['source'], headline=article['headline'], link=article['link'])
            news.save()

    def getFromDb(self, query = None):
        news = News.objects.filter(query=(query if query else 'list'))
        serializer = NewsSerializer(news)
        return serializer.data

    def get(self, request):
        query = request.query_params.get('query', None)
        news = self.getFromDb(query)
        if (not news):
            if (query):
                news = self.requestNewsApi(query)
                news += self.requestRedditApi(query)
                self.storeInDb(news, query)
            else:
                news = self.requestNewsApi()
                news += self.requestRedditApi()
                self.storeInDb(news)
            
        return Response(news)

# class NewsListView(ListAPIView):
#     queryset = News.