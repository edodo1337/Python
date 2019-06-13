from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponse
from django.views.generic import View
from .forms import *


class ObjectDetailMixin(View):

    model = None
    template = None
    obj = None

    def post(self, request, slug):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.user = request.user
            form.article = self.obj
            form.save()



    def get(self, request, slug):
        self.obj = get_object_or_404(self.model, slug__iexact=slug)
        comments = Comment.objects.filter(article=obj)
        form = CommentForm()
        return render(request, self.template, context={self.model.__name__.lower() : obj, 'detail':True, 'comments':comments, 'form':form})