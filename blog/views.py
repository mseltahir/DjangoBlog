from django.shortcuts import render


def blog_page(request):
    context = {
        'title': 'Blog'
    }
    return render(request, 'blog/blog.html', context=context)
