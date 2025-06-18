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
            return redirect('home')

    context = {'RegisterForm': form,}

    return render(request, 'register.html', context)


def dashboard(request):
    return render(request, 'dashboard.html')
