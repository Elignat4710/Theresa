from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
import redis
from django.http import HttpResponseRedirect


class View(ListView):
    context_object_name = 'products_list'
    queryset = Product.objects.all()
    template_name = 'theresa_app/index.html'

    def post(self, request, *args, **kwargs):
        r = redis.Redis()
        r.lpush(
            'theresa:start_urls',
            'https://www.mytheresa.com/en-us/clothing/dresses/short.html?'
            )
        return HttpResponseRedirect('/')
