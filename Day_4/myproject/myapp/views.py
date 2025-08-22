from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def testpaper(request):
    que1 = "Select your branch :"
    A1 = "AI-DS"
    B1 = "ECE"
    C1 = "MECH"
    D1 = "CIVIL"
    que2 = "Select your year"
    A2 = "1st"
    B2 = "2nd"
    C2 = "3rd"
    D2 = "4Th"
    que3 = "Select semester"
    A3 = "odd"
    B3 = "even"
    context = {
        "questions":[{"que":que1, "options":[A1, B1, C1, D1]},{"que":que2, "options":[A2, B2, C2, D2]},{"que":que3, "options":[A3, B3]}]
    }
    template = loader.get_template("testpaper.html")
    res = template.render(context, request)
    return HttpResponse(res)

def eligible(request):
    template = loader.get_template("voting.html")
    context = {
        "name" : "Rishabh",
        "age" : 20
    }
    res = template.render(context, request)
    return HttpResponse(res)

def result(request):
    template = loader.get_template("result.html")
    context = {
        "name" : "Rishabh",
        "dept" : "AI-DS"
    }
    res = template.render(context, request)
    return HttpResponse(res)