from .models import Post
from django import forms


class createPost(forms.Form):

    class Meta:
        Model = Post
        Fields = ['title','content']

