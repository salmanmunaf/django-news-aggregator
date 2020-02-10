from django.urls import include, path
from rest_framework import routers
from .views import NewsView

# router = routers.DefaultRouter()
# router.register('news', views.NewsView, basename='news')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('news/', NewsView.as_view())
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]