# from django.contrib.auth.models import User
from django import forms

from .models import Post


class PostCreateForm(forms.ModelForm):
    """Enable users to create posts"""

    class Meta:
        model = Post
        fields = ('post', 'caption')
