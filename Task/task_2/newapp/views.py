from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def products(request):
    template = loader.get_template('index.html')
    context = {
        'products': [{"name":"Apple","price":100,"discount":10,"discounted_price":90},{"name":"Pineapple","price":180,"discount":5, "discounted_price":171}]
    }
    res = template.render(context, request)
    return HttpResponse(res)