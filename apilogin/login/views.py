from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# from product.models import Product

def show(request):
   
    return render(request,"index.html")
    #return HttpResponse("welcome to show")

