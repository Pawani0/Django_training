from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testpaper(request):
    return HttpResponse('<h1>This is test paper page</h1>')

def result(request):
    return HttpResponse('<h1>This is result page</h1>')