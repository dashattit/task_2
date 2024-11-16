from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import AddUserCreatingForm, AddUserLoginForm
from .models import AddUser
from django.views import generic
from django.views.generic.edit import FormView

def index(request):
    return render(request, 'index.html')

class Register(generic.CreateView):
    template_name = 'catalog/register.html'
    form_class = AddUserCreatingForm
    success_url = reverse_lazy('login')

class Login(FormView):
    template_name = 'catalog/login.html'
    form_class = AddUserLoginForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "Неверное имя пользователя или пароль.")
            return self.form_invalid(form)  # Возвращаем форму с ошибками


class UserProfileListView(generic.ListView):
    model = AddUser
    template_name = 'catalog/profile.html'

def logout_user(request):
    logout(request)
    return render(request, 'catalog/logout.html')

def create_user(request):
    if request.method == 'POST':
        form = AddUserCreatingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'catalog/login.html')
    else:
        form = AddUserCreatingForm()
        return render(request, 'catalog/login.html', {'form': form})
