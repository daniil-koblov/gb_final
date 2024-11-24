from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'recipe_app'

urlpatterns = [
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('', views.get_five_recipes, name='index'),
    path('get_recipe/<str:id_recipe>/', views.get_recipe, name='get_recipe'),
    path('edit_recipe/<str:id_recipe>/', views.edit_recipe, name='edit_recipe'),
    path('get_full_recipes/', views.get_full_recipes, name='get_full_recipes'),
]
if settings.DEBUG:  # Только в режиме разработки
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
