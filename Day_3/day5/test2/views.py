from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def testpaper(request):
    que1="What is the largest planet in our solar system?"
    A1="Mars"
    B1="Saturn"
    C1="Jupiter"
    D1="Neptune"
    que2="Who was the first emperor of Rome?"
    A2="Julius Caesar"
    B2="Constantine"
    C2="Nero"
    D2="Augustus"
    que3="What is the world's longest river?"
    A3="The Yangtze River"
    B3="The Nile River"
    C3="The Amazon River"
    D3="The Mississippi River"
    que4="Which famous artist is known for cutting off part of his own ear?"
    A4="Claude Monet"
    B4="Vincent van Gogh"
    C4="Pablo Picasso"
    D4="Leonardo da Vinci"
    que5="In the 'Lord of the Rings' trilogy, what is the name of the wizard who guides the Fellowship?"
    A5="Saruman"
    B5="Dumbledore"
    C5="Gandalf"
    D5="Merlin"
    
    temp = loader.get_template('testpaper.html')
    return HttpResponse(temp.render({'Que1':que1,'A1':A1,'B1':B1,'C1':C1,'D1':D1,
                                     'Que2':que2,'A2':A2,'B2':B2,'C2':C2,'D2':D2,
                                     'Que3':que3,'A3':A3,'B3':B3,'C3':C3,'D3':D3,
                                     'Que4':que4,'A4':A4,'B4':B4,'C4':C4,'D4':D4,
                                     'Que5':que5,'A5':A5,'B5':B5,'C5':C5,'D5':D5}))
