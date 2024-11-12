from django.urls import path
from .views import index, UserProfileListView
from . import views


urlpatterns = [
    path('catalog/', index, name='index'),
    path('catalog/register/', views.Register.as_view(), name='register'),
    path('catalog/login/', views.Login.as_view(), name='login'),
    path('catalog/profile/', UserProfileListView.as_view(), name='profile'),
]