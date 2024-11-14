from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings

class AddUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    patronym = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    password_confirm = models.CharField(max_length=100, blank=True)

    groups = models.ManyToManyField(
        Group, related_query_name='adduser',
        blank=True, help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True, help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.username



class Request(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='requests',
        verbose_name="Пользователь"
    )

    title = models.CharField(max_length=200, verbose_name="Напишите название заявки")
    description = models.TextField(verbose_name="Напишите к заявке описание")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Выберите категорию заявки")
    image = models.FileField(
        upload_to='requests',
        validators=[validate_image],
        verbose_name="Загрузите фото заявки"
    )
    LOAN_STATUS = (
        ('n', 'Новая'),
        ('a', 'Принято в работу'),
        ('s', 'Выполнено'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, verbose_name='Статус заявки', help_text='Статус заявки')
    created_at = models.DateTimeField(auto_now_add=True, help_text="Дата и время создания заявки")

