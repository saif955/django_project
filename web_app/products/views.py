from django.shortcuts import render
from django.http import HttpResponse

generic_response = 123


def index(request):
    return HttpResponse('Hello')


def new(request):
    return HttpResponse('new response')


def practise(request):
    return HttpResponse(generic_response)
