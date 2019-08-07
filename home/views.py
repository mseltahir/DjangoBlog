from django.shortcuts import render


def home_page(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'home/home.html', context=context)
