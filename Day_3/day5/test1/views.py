from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def home(request):
    temp = loader.get_template('home.html')
    return HttpResponse(temp.render())

def ml(request):
    temp = loader.get_template('machine_learning.html')
    return HttpResponse(temp.render())