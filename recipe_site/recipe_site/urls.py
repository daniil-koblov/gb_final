from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipe_app.urls', namespace='recipe_app')),
    path('user/', include('users_app.urls', namespace='users_app')),
]
if settings.DEBUG:  # Только в режиме разработки
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
