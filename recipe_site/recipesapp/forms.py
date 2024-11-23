from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'steps', 'preparation_time', 'image', 'categories']
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'steps': 'Процесс готовки',
            'preparation_time': 'Время приготовления(в минутах)',
            'image': 'Изображение',
            'categories': 'Категории',
        }
