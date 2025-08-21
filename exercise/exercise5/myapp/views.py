from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def gfg(request):
    name = "Mr. Sandeep Jain"
    temp = loader.get_template("gfg.html")
    return HttpResponse(temp.render({'name':name}))

def linkedin(request):
    name = "Reid Garrett Hoffman"
    temp = loader.get_template("linkedin.html")
    return HttpResponse(temp.render({'name':name}))

def facebook(request):
    name = "Mark Zuckerberg"
    temp = loader.get_template("facebook.html")
    return HttpResponse(temp.render({'name':name}))