from django.db import models
from django.contrib.auth.models import AbstractUser

class AddUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    patronym = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    password_confirm = models.CharField(max_length=100, blank=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.username

# Create your models here.
