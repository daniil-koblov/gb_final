from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipe_app.urls', namespace='recipe_app')),
    path('user/', include('users_app.urls', namespace='users_app')),
]
