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


