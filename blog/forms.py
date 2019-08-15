from django import forms
from .models import Post


class PostForm(forms.Form):
    author = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Your Name'}))
    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Post Title'}))
    content = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Content'}))
