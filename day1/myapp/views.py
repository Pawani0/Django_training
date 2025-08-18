from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myfunction(request):
    s = "<h1>Rishabh Pawani</h1>"
    return HttpResponse(s)