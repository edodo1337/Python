from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
def hello(request):
    return(HttpResponse('<h1>Hello</h1>'))


class HomePageView(TemplateView):
    template_name = 'index.html'
