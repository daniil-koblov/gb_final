from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно!")
            return redirect('recipe_app:index')
    else:
        form = RegisterForm()
    return render(request, 'users_app/register.html', {'form': form})


def authorization(request):
    if request.method == 'POST':
        print(f"POST данные: {request.POST}")
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Введённые логин и пароль: {username}, {password}")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Вход выполнен успешно!")
            print("Вход выполнен успешно!")
            return redirect('recipe_app:index')
        else:
            print("authenticate() вернул None")
            messages.error(request, "Ошибка входа. Проверьте логин и пароль.")
    form = LoginForm()
    return render(request, 'users_app/authorization.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, "Выход из системы выполнен успешно!")
    return redirect('recipe_app:index')


