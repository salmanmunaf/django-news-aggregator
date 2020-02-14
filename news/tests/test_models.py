from django.test import TestCase
from ..models import News


class NewsTest(TestCase):
    """ Test module for News model """

    def setUp(self):
        News.objects.create(
            query='facebook', request_date='2020-02-13', headline='Stephen King quits Facebook over concerns of `false information`', link='https://www.cnn.com/2020/02/02/us/stephen-king-quits-facebook-trnd/index.html', source='reddit')
        News.objects.create(
            query='bitcoin', request_date='2020-02-13', headline='Bitcoin investors may be out $190 million after the only guy with the password dies, firm says', link='https://www.miamiherald.com/news/nation-world/world/article225501940.html', source='reddit')

    def test_news_headline(self):
        news_facebook = News.objects.get(query='facebook')
        news_bitcoin = News.objects.get(query='bitcoin')
        self.assertEqual(
            news_facebook.get_headline(), "Stephen King quits Facebook over concerns of `false information`")
        self.assertEqual(
            news_bitcoin.get_headline(), "Bitcoin investors may be out $190 million after the only guy with the password dies, firm says")