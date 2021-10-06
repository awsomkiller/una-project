from django.shortcuts import render
from .models import product  

def productviews(request):
    allproduct = product.objects.all()
    return render(request, 'index.html', {'productdata':allproduct})
