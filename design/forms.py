from django import forms
from .models import AddUser
from django.contrib.auth import authenticate



class AddUserCreatingForm(forms.ModelForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput()
    )
    email = forms.CharField(
        max_length=100,
        widget=forms.EmailInput()
    )
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput()
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput()
    )
    patronym = forms.CharField(
        max_length=100,
        widget=forms.TextInput()
    )
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Пароли не совпадают")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        if commit:
            user.save()
        return user

    class Meta:
        model = AddUser
        fields = ("username", "email", "first_name", "last_name", "patronym")


class AddUserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'})
    )
    password = forms.CharField(widget=forms.PasswordInput)