from django.urls import path
from .views import index, UserProfileListView
from . import views

# app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/register/', views.Register.as_view(), name='register'),
    path('catalog/login/', views.Login.as_view(), name='login'),
    path('catalog/logout/', views.logout_user, name='logout'),
    path('catalog/profile/', UserProfileListView.as_view(), name='profile'),
]


