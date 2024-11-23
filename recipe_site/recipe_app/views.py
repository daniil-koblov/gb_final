from django.shortcuts import render, redirect
from .models import Author, Recipe, Category
from .forms import AuthorForm, RecipeForm


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            Author.objects.create(
                name=form_data['name'],
                email=form_data['email']
            )
    else:
        form = AuthorForm()
    authors = Author.objects.all()
    context = {'authors': authors, 'form': form}
    return render(request, 'recipe_app/register_authors.html', context)


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.cleaned_data
            Recipe.objects.create(
                title=form_data['title'],
                description=form_data['description'],
                ingredients=form_data['ingredients'],
                steps_cooking=form_data['steps_cooking'],
                time_cooking = form_data['time_cooking'],
                image_dish=form_data['image'],
                author=Author.objects.get(id=form_data['author'])
            )
    else:
        form = RecipeForm()
    recipes = Recipe.objects.all()
    context = {'recipes': recipes, 'form': form}
    return render(request, 'recipe_app/create_recipes.html', context)
