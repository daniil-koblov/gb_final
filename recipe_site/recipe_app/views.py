import random
from django.shortcuts import render, redirect
from .models import Recipe, Category
from .forms import RecipeForm
FRIST_ID = 1
SIX_ID = 6


def add_recipe(request):
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
    context = {'recipes': recipes, 'form': form}
    return render(request, 'recipe_app/create_recipes.html', context)


def get_five_recipes(request, id_recipe: int):
    for count in range(FRIST_ID, SIX_ID):
        id_recipe = random.randint(1, 10)
        recipe = get_object_or_404(Recipe, id=id_recipe)
        recipe.__str__()
        context = {
            'title': recipe.title,
            # 'author': recipe.author,
            'description': recipe.description,
            'time_cooking': recipe.time_cooking,
        }
        count += 1
        return render(request, 'recipe_app/index.html', context)

