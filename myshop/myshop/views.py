from django.http.response import HttpResponse #ADD THIS
from django.shortcuts import render
from django.conf import settings

def welcome(request):
    num1 = 5
    num2 = 10
    name = num1+num2
    imgpath = str(settings.BASE_DIR) + "\imagecontainer\okia.jpg"
    return render(request, 'index.html', {'providedname':name, 'image':imgpath})

