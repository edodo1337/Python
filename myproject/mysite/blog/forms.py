from django import forms
from .models import *
from django.core.exceptions import ValidationError




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body','image']