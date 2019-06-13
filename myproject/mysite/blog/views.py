from __future__ import absolute_import, division, unicode_literals
from .models import *
from django.views.generic import View, TemplateView, ListView
from .utils import *
from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)
        context['articles'] = self.model.objects.all()
        return context

class ArticleDetailView(ObjectDetailMixin, View):
    model = Article
    template = 'blog/article_detail.html'

