from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.text import slugify
from time import time
from PIL import Image
import os



class Category(models.Model):
    title = models.CharField(max_length=15)
    slug = models.SlugField()

    def __str__(self):
        return self.title

def generate_filename(instance, filename):
    ext = filename[filename.rfind('.') + 1:]
    filename = 'media/images/'+instance.slug + '/' + filename
    return filename


class Article(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    image = models.ImageField(upload_to=generate_filename)
    body = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET('anonymous'), blank=True)
    body = models.TextField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    image = models.ImageField(upload_to=generate_filename, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
