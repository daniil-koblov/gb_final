from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'users_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('authorization/', views.authorization, name='authorization'),
    path('logout/', views.logout_user, name='logout'),
]
if settings.DEBUG:  # Только в режиме разработки
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)