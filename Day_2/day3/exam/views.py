from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greeting(request):
    return HttpResponse('<h1>Hello this is my website</h1>')

def about(request):
    return HttpResponse('<h1>Hello this is my website about page</h1>')

def contact(request):
    return HttpResponse('<h1>Hello this is my website contact page</h1>')