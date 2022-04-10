from itertools import product
from django.shortcuts import render

from .models import Category,Product

def Categories (request):
    return{
        'categories':Category.object.all()
    }

def all_products(request):
    products=Product.objects.all()
    return render (request,'store/home.html',{'products':products})
