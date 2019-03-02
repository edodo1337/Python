from django.conf.urls import urls
from . import views

urlpatterns = [
    path(r'^$', views.index, name = "index"),

]
