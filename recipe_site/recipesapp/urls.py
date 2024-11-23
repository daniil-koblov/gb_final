from django.conf import settings  # not for prod
from django.conf.urls.static import static  # not for prod
from django.urls import path

from .views import login_view, register, logout_view, home_view, recipe_detail, recipe_create_view, recipe_update_view, \
    recipe_list_view, user_recipes_view, recipe_delete_view

urlpatterns = [
                  path('', home_view, name='home'),
                  path('register/', register, name='register'),
                  path('login/', login_view, name='login'),
                  path('logout/', logout_view, name='logout'),
                  path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
                  path('recipe/new/', recipe_create_view, name='recipe_create'),
                  path('recipe/<int:id>/edit/', recipe_update_view, name='recipe_update'),
                  path('recipes/', recipe_list_view, name='recipe_list'),
                  path('myrecipes/', user_recipes_view, name='user_recipes'),
                  path('recipe/<int:id>/delete/', recipe_delete_view, name='recipe_delete'),
              ]
