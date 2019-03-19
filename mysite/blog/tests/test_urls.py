from django.test import TestCase
from django.urls import reverse, resolve
from blog.views import *

class TestUrls(TestCase):

    def test_list_url_is_resolved(self):
        url = reverse('post_list_url')
        print(resolve(url))
        self.asserEquals(resolve(url).func, post_list_url)
