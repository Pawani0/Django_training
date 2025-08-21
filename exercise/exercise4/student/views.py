from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def student(request):
    template = loader.get_template('student.html')
    context = {"name":"Rishabh Pawani", "branch":"AI-DS", "p":75, "c":80, "m":78, "en":68, "hi":90, "total":75+80+78+68+90, "percent":(75+80+78+68+90)/5}
    return HttpResponse(template.render(context, request))