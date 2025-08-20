from django.shortcuts import render
from django.http import HttpResponse

def result(request):
    return HttpResponse("<h1><B>Vth semester result</h1>")

def result2(request):
    s = "<h1>MBA result</h1>"
    return HttpResponse(s)
