from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
import requests, json

from .models import News

TOKEN = '4ee7621bf86f4cc7ad34b55089e71e0d'

class NewsView(APIView):
    def get(self, request):
        headers = { 'Authorization' : 'Basic ' + TOKEN }
        r = requests.get('https://newsapi.org/v2/top-headlines?sources=bbc-news', headers=headers)
        news = json.loads(r.text)
        # news = News.objects.all()
        return Response({"news": news})