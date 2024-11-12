from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import AddUserCreatingForm
from .models import AddUser
from django.views import generic

def index(request):
    return render(request, 'index.html')


class Register(generic.CreateView):
    template_name = 'catalog/register.html'
    form_class = AddUserCreatingForm
    success_url = reverse_lazy('login')


# Create your views here.
