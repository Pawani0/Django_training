from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sistec_web(request):
    return HttpResponse("<a href = 'https://www.sistec.ac.in/'>Click here to visit SISTec</a>")