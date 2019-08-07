from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)


class Category(models.Model):
    name = models.CharField(max_length=60)
    post = models.ManyToManyField(Post, related_name='categories')
