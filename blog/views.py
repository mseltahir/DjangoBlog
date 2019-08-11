from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from blog.models import Post, Comment
from blog.forms import CommentForm, PostForm


def blog_page(request):
    context = {
        'title': 'Blog',
        'posts': Post.objects.all().order_by('-created_on')
    }
    return render(request, 'blog/blog.html', context=context)


def blog_new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author'],
                content=form.cleaned_data['content']
            )
            post.save()
            return redirect(f'/blog/{post.pk}')
    else:
        form = PostForm()

    context = {
        'title': 'New',
        'form': form
    }
    return render(request, 'blog/new_post.html', context=context)


def blog_detail(request, pk):

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment(author=form.cleaned_data['author'],
                    comment=form.cleaned_data['comment'],
                    post=Post.objects.get(pk=pk)).save()
            return HttpResponseRedirect(f'{pk}')
    else:
        form = CommentForm()

    context = {
        'title': 'Blog',
        'post': Post.objects.get(pk=pk),
        'form': form
    }
    return render(request, 'blog/detail.html', context=context)


def blog_category(request, category):
    context = {
        'title': 'Blog Categories',
        'category': category,
        'posts': Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    }
    return render(request, 'blog/category.html', context=context)
