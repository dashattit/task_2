from django.urls import path
from . import views
from .views import UserProfileListView


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', UserProfileListView.as_view(), name='profile'),
]


