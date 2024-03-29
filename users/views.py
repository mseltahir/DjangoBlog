from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(
                request, f'Account for {username} was created successfully. Now you can Login!')
            return redirect('blog:blog_page')
    else:
        form = UserRegisterForm()
    context = {
        'title': 'Sign Up',
        'form': form
    }
    return render(request, 'users/register.html', context=context)


@login_required
def profile(request):
    context = {
        'title': 'Profile'
    }
    return render(request, 'users/profile.html', context)
