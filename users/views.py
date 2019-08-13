from django.shortcuts import render, redirect
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:blog_page')
    else:
        form = UserRegisterForm()
    context = {
        'title': 'Sign Up',
        'form': form
    }
    return render(request, 'users/register.html', context=context)
