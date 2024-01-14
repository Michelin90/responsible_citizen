from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.mail import send_mail
from django.db import models


class CustomUserManager(BaseUserManager):
    """Класс менеджера кастомной модели пользователя."""

    def create_user(self, email, password):
        if email is None:
            raise TypeError('У пользователя должен быть email.')
        if password is None:
            raise TypeError('У пользователя должен быть пароль.')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Кастомная модель пользователя."""

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
        unique=True,
        db_index=True
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
    is_staff = models.BooleanField(
        verbose_name='Статус пользователя',
        default=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    is_active = models.BooleanField(
        verbose_name='Статус активности пользователя',
        default=False
    )

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def get_full_name(self):
        """Возвращает ФИО пользователя.

        Возвращает значения полей first_name, last_name, middle_name,
        разделенные пробелами.
        """
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    def get_short_name(self):
        """Возвращает значение поля first_name для выбранного пользователя."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Отправляет email выбранному пользователю."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class EmailConfirmation(models.Model):
    """Модель хранения данных для проверки валидности ссылки-подтверждения."""

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(
        verbose_name='Токен верификации почты',
        max_length=25
    )
    created_at = models.DateField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
