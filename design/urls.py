from django.urls import path
from .views import index
from . import views
from design_pro.design_pro.urls import urlpatterns

urlpatterns = [
    path('catalog/', index, name='index'),
    path('catalog/register/', views.Register.as_view(), name='register'),
]