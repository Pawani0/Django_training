from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def lnct_web(request):
    return HttpResponse("<a href = 'https://lnct.ac.in/'>Click here to visit LNCT</a>")