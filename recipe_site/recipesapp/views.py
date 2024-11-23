from random import shuffle

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect

from .forms import RecipeForm
from .models import Recipe


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})


@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        return render(request, 'user/logout.html')


def home_view(request):
    recipes = list(Recipe.objects.all())  # Not for large bd, cuz metod getiing all rows from "Recipe" table
    shuffle(recipes)
    recipes = recipes[:5]
    return render(request, 'home.html', {'recipes': recipes})


@login_required
def recipe_create_view(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipe_form.html', {'form': form})


def recipe_update_view(request, id):
    recipe = Recipe.objects.get(id=id)
    if recipe.author != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe_form.html', {'form': form, 'recipe': recipe})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes_detail.html', {'recipe': recipe})


def recipe_list_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})


@login_required
def user_recipes_view(request):
    recipes = Recipe.objects.filter(author=request.user)
    return render(request, 'user_recipes.html', {'recipes': recipes})


@login_required
def recipe_delete_view(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if recipe.author != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'recipe_confirm_delete.html', {'recipe': recipe})
