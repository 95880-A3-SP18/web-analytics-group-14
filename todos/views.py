
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.db import IntegrityError
from django.shortcuts import render, render_to_response
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from .models import TodoItem, Market
from django.utils.safestring import mark_safe


class IndexView(ListView):
    model = TodoItem

def index(request):
    response = render(request,'todos/index.html')
    return response


class IndexView(ListView):
    model = TodoItem

def index(request):
    response = render(request,'todos/index.html')
    return response


class MarketView(ListView):
    model = TodoItem
    template_name = 'markets.html'
def market(request):
    pageHtml = "hello world"
    ret = {"pageHtml": pageHtml}
    return render(request, "markets.html", ret)


class CoinView(ListView):
    model = TodoItem
    template_name = 'coin.html'


class TweetView(ListView):
    model = TodoItem
    template_name = 'tweets.html'


class MapView(ListView):
    model = TodoItem
    template_name = 'heatmap.html'