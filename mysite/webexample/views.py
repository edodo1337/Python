from django.shortcuts import render
from django.Http import HttpResponse


def index (request):
    return(HttpResponse("<h3>Hello</h3">))




# Create your views here.
