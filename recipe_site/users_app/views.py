from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно!")
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'users_app/register.html', {'form': form})


def authorization(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Вход выполнен успешно!")
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'users_app/authorization.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, "Выход из системы выполнен успешно!")
    return redirect('index')

