from . import views
from django.urls import path

urlpatterns = [
    path('create_recipe/', views.add_recipe, name='add_recipe'),
    path('', views.get_five_recipes, name='index')
]
