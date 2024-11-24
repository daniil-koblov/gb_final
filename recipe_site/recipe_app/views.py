import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Category
from .forms import RecipeForm
from django.http import HttpResponse
FRIST_ID = 1
SIX_ID = 3


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            form_data = form.cleaned_data
            Recipe.objects.create(
                title=form_data['title'],
                description=form_data['description'],
                ingredients=form_data['ingredients'],
                steps_cooking=form_data['steps_cooking'],
                time_cooking=form_data['time_cooking'],
                image_dish=form_data['image'],
                # author=Author.objects.get(id=form_data['author'])
            )
    else:
        form = RecipeForm()
    recipes = Recipe.objects.all()
    context = {'media': recipes, 'form': form}
    return render(request, 'recipe_app/create_recipes.html', context)


def get_five_recipes(request):
    recipes = []
    added_recipe_ids = set()
    count = 0
    while count < 5:
        id_recipe = random.randint(1, 5)
        if id_recipe not in added_recipe_ids:
            recipe = get_object_or_404(Recipe, id=id_recipe)
            recipes.append({
                'title': recipe.title,
                'description': recipe.description,
                'time_cooking': recipe.time_cooking,
                'id_recipe': recipe.id,
            })
            added_recipe_ids.add(id_recipe)
            count += 1

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
    }
    print(recipe.image_dish)
    return render(request, 'recipe_app/get_recipe.html', context)

# For admin panel
