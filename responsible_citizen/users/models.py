from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.TextField(
        unique=True,
        blank=True
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150
    )
    middle_name = models.CharField(
        verbose_name='Отчество',
        max_length=150,
        blank=True
    )
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        unique=True
    )
    address = models.CharField(
        verbose_name='Адресс проживания',
        max_length=250
    )
    phone_number = models.CharField(
        verbose_name='Номер телефона',
        max_length=12,
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
