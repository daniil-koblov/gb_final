from django import forms
from .models import Author, Recipe, Category


class AuthorForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        max_length=50,
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя автора'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'})
    )
    password = forms.CharField()


class RecipeForm(forms.Form):
    title = forms.CharField(
        min_length=2,
        max_length=60,
        label='Название рецепта',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название рецепта'})
    )
    description = forms.CharField(
        max_length=200,
        label='Описание рецепта',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание рецепта'})
    )
    ingredients = forms.CharField(
        min_length=2,
        max_length=200,
        label='Ингредиенты',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ингредиенты'})
    )
    steps_cooking = forms.CharField(
        max_length=200,
        label='Шаги приготовления',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Запишите шаги приготовления'})
    )
    time_cooking = forms.CharField(
        max_length=30,
        label='Время приготовления',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Опишите время приготовления'})
    )
    image_dish = forms.ImageField(
        label='Изображение рецепта',
        widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Загрузите изображение рецепта'})
    )



