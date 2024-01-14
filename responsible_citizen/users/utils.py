from secrets import token_urlsafe
from urllib.parse import urljoin

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .models import CustomUser, EmailConfirmation


def create_confirmation_link(user: CustomUser) -> str:
    """Формирует ссылку-подтверждение."""
    confirmation = EmailConfirmation.objects.create(
        user=user, token=token_urlsafe(25)
    )
    uidb64 = urlsafe_base64_encode(str(user.pk).encode())
    confirmation_link = reverse(
        'email_confirmation',
        kwargs={'uidb64': uidb64, 'token': confirmation.token}
    )
    base_url = settings.BASE_URL
    full_link = urljoin(base_url, confirmation_link)
    return full_link


def send_confirmation_link_to_email(user: CustomUser) -> None:
    """Отправляет ссылку-подтверждение.

    Осуществляет отправление ссылки-подтверждения на указанный
    при регистрации пользоваетля адерсс электронной почты.
    """
    confirmation_link = create_confirmation_link(user)
    user.email_user(
        subject='Подтверждение почты',
        message=(
            f'Для подтверждения email перейдите по ссылке: {confirmation_link}'
        ),
        from_email=settings.EMAIL_HOST_USER
    )


def confirm_email(uidb64: str, token: str) -> None:
    """Проверяет валидность подтверждающей ссылки.

    В случае успеха активирует пользовательский аккаунт.
    """
    uid = urlsafe_base64_decode(uidb64)
    user = get_object_or_404(CustomUser, pk=uid)
    confirmation = get_object_or_404(
        EmailConfirmation, user=user, token=token
    )
    user.is_active = True
    user.save()
    confirmation.delete()
