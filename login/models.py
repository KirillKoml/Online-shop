from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True,
                              verbose_name='Адрес электронной почты')
    avatar = models.ImageField(upload_to="users/avatar/",
                               verbose_name="Аватар пользователя",
                               null=True,
                               blank=True)
    phone = models.CharField(max_length=15,
                             verbose_name='телефон',
                             blank=True,
                             null=True,
                             help_text='Введите номер телефона')
    country = models.CharField(max_length=15,
                               verbose_name='Страна',
                               null=True,
                               blank=True)
    token = models.CharField(max_length=60,
                             verbose_name='Код подтверждения, который отправляется на почту',
                             null=True,
                             blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
