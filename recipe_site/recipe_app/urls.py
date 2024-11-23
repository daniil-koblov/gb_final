from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.add_author, name='add_author'),
    path('create_recipe/', views.add_recipe, name='add_recipe'),
]
