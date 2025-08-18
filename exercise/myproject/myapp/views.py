from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myfunction(request):
    s = "<h1>SISTec</h1>"
    return HttpResponse(s)

def department(request):
    s = "<h1>Department is CSE(AI-DS)</h1>"
    return HttpResponse(s)
