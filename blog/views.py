from django.shortcuts import render
from blog.models import Post


def blog_page(request):
    context = {
        'title': 'Blog',
        'posts': Post.objects.all().order_by('-created_on')
    }
    return render(request, 'blog/blog.html', context=context)


def blog_detail(request, pk):
    context = {
        'title': 'Blog',
        'post': Post.objects.get(pk=pk)
    }
    return render(request, 'blog/detail.html', context=context)


def blog_category(request, category):
    context = {
        'title': 'Blog',
        'category': category,
        'posts': Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    }
    return render(request, 'blog/category.html', context=context)
