

from django.contrib import admin
from django.urls import path
from .views import *
from django.views.generic.base import TemplateView
urlpatterns = [
        path('', ArticleListView.as_view()),
        path('<slug:slug>/', ArticleDetailView.as_view(), name='article_detail')
]
