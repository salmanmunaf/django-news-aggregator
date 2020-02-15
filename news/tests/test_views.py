import json, datetime
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import News
from ..serializers import NewsSerializer


# initialize the APIClient app
client = Client()

class GetNewsTest(TestCase):
    """ Test module for GET news API """

    def setUp(self):
        News.objects.create(
            query='facebook', request_date='2020-02-13', headline='Stephen King quits Facebook over concerns of `false information`', link='https://www.cnn.com/2020/02/02/us/stephen-king-quits-facebook-trnd/index.html', source='reddit')
        News.objects.create(
            query='bitcoin', request_date='2020-02-13', headline='Bitcoin investors may be out $190 million after the only guy with the password dies, firm says', link='https://www.miamiherald.com/news/nation-world/world/article225501940.html', source='reddit')

    def test_get_news(self):
        # get API response
        response = client.get('/news')
        # get data from db
        news = News.objects.filter(query='list', request_date=datetime.date.today())
        serializer = NewsSerializer(news, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_news(self):
        # get API response
        response = client.get('/news', {'query' : 'bitcoin'})
        # get data from db
        news = News.objects.filter(query='bitcoin', request_date=datetime.date.today())
        serializer = NewsSerializer(news, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)