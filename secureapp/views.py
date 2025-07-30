from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CreateUserForm


def home(request):
    return render(request, 'index.html')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('two_factor:login')

    context = {'RegisterForm': form,}

    return render(request, 'register.html', context)


@login_required(login_url='two_factor:login')
def dashboard(request):
    return render(request, 'dashboard.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


def account_locked(request):
    return render(request, 'account_locked.html')
