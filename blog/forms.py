from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(max_length=3000)
    author = forms.CharField(max_length=60)


class CommentForm(forms.Form):
    author = forms.CharField(max_length=60)
    comment = forms.CharField(max_length=1200)
