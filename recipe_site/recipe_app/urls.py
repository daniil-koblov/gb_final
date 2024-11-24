from . import views
from django.urls import path

app_name = 'recipe_app'

urlpatterns = [
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('', views.get_five_recipes, name='index'),
    path('get_recipe/<int:id_recipe>/', views.get_recipe, name='get_recipe')
]
