import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm
from django.http import HttpResponse
from django.db.models import Count
from random import sample
FRIST_ID = 1
SIX_ID = 3


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            Recipe.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                ingredients=form.cleaned_data['ingredients'],
                steps_cooking=form.cleaned_data['steps_cooking'],
                time_cooking=form.cleaned_data['time_cooking'],
                image_dish=form.cleaned_data['image_dish'],
            )
            return redirect('recipe_app:index')
    else:
        form = RecipeForm()

    context = {'form': form}
    return render(request, 'recipe_app/create_recipe.html', context)


def get_five_recipes(request):
    recipes_queryset = Recipe.objects.all()
    if recipes_queryset.count() <= 5:
        recipes = recipes_queryset
    else:
        recipe_ids = list(recipes_queryset.values_list('id', flat=True))
        random_ids = sample(recipe_ids, 5)
        recipes = Recipe.objects.filter(id__in=random_ids)

    context = {
        'recipes': recipes,
    }
    return render(request, 'recipe_app/index.html', context)


def get_recipe(request, id_recipe):
    recipe = get_object_or_404(Recipe, id=id_recipe)
    context = {
        'title': recipe.title,
        'description': recipe.description,
        'ingredients': recipe.ingredients,
        'steps_cooking': recipe.steps_cooking,
        'time_cooking': recipe.time_cooking,
        'image_dish': recipe.image_dish,
        'recipe': recipe,  # Передаём объект recipe
    }
    return render(request, 'recipe_app/get_recipe.html', context)


def edit_recipe(request, id_recipe):
    recipe = get_object_or_404(Recipe, id=id_recipe)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe.title = form.cleaned_data['title']
            recipe.description = form.cleaned_data['description']
            recipe.ingredients = form.cleaned_data['ingredients']
            recipe.steps_cooking = form.cleaned_data['steps_cooking']
            recipe.time_cooking = form.cleaned_data['time_cooking']
            if 'image_dish' in request.FILES:
                recipe.image_dish = request.FILES['image_dish']
            recipe.save()
            return redirect('recipe_app:get_recipe', id_recipe=recipe.id)
    else:
        form = RecipeForm(initial={
            'title': recipe.title,
            'description': recipe.description,
            'ingredients': recipe.ingredients,
            'steps_cooking': recipe.steps_cooking,
            'time_cooking': recipe.time_cooking,
        })
    context = {'form': form, 'recipe': recipe}
    return render(request, 'recipe_app/edit_recipe.html', context)


def get_full_recipes(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'recipe_app/get_full_recipes.html', context)
