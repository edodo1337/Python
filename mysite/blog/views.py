from django.shortcuts import render
from django.http import HttpResponse
def posts_list(request):
    return(HttpResponse("<h2>Hello</h2>"))# Create your views here.
