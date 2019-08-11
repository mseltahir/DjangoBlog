from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)


class Category(models.Model):
    name = models.CharField(max_length=60)
    post = models.ManyToManyField(Post, related_name='categories')


class Comment(models.Model):
    author = models.CharField(max_length=60)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        'blog.Post', on_delete=models.CASCADE, related_name='comments', null=True)
