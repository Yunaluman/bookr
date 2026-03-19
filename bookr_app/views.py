# Create your views here.
from django.http import HttpResponse
from backoffice.models import Product
from django.shortcuts import render


def index(request):
    product = Product.objects.get(pk=2)
    return render(request, 'index.html', {'product': product})
