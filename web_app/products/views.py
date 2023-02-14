from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

generic_response = 123


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('new response')


def practise(request):
    return HttpResponse(generic_response)
