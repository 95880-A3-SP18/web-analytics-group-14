from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('markets', views.MarketView.as_view(), name='markets'),
    path('coin', views.CoinView.as_view(), name='coin'),
    path('tweets', views.TweetView.as_view(), name='tweet'),
    path('heatmap', views.MapView.as_view(), name='heatmap'),
]
