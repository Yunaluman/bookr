from django.shortcuts import render
from django.http import HttpResponse
from backoffice.models import Product


def index(request):
    return HttpResponse("Backoffice")


def getProduct(request):
    product = Product.objects.all()
    product_str = ""
    
    for p in product:
        product_str += p.name + ", "
    
    return HttpResponse("Liste des produits : " + product_str)
