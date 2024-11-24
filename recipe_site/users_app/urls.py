from . import views
from django.urls import path

# app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('authorization/', views.authorization, name='authorization'),
    path('logout/', views.logout, name='logout'),
]
