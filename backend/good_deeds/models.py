from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class GoodDeed(models.Model):
    """Доброе дело."""
    CONSIDERATION = 'consideration'
    EXECUTED = 'executed'
    NOT_EXECUTED = 'not_executed'
    IN_PROGRESS = 'in_progress'
    ROADS = 'roads'
    LIGHTING = 'lighting'
    IMPROVMENT = 'improvment'
    PROPERTY = 'property'
    OTHER = 'other'
    STAGE_CHOICES = [
        (CONSIDERATION, 'На рассмотрении'),
        (EXECUTED, 'Выполнено'),
        (NOT_EXECUTED, 'Не выполнено'),
        (IN_PROGRESS, 'В процессе выполнения')
    ]
    THEME_CHOICES = [
        (ROADS, 'Дороги'),
        (LIGHTING, 'Уличное освещение'),
        (IMPROVMENT, 'Благоустройство'),
        (PROPERTY, 'Содержание имущества'),
        (OTHER, 'Иное')
    ]
    theme = models.CharField(
        verbose_name='Тема обращения',
        max_length=10,
        choices=THEME_CHOICES,
    )
    description = models.TextField(verbose_name='Текст обращения')
    sender = models.ForeignKey(
        User,
        verbose_name='Отправитель обращения',
        on_delete=models.CASCADE,
        related_name='good_deeds'
    )
    stage = models.CharField(
        verbose_name='Статус исполнения',
        choices=STAGE_CHOICES,
        default=CONSIDERATION,
        max_length=13
    )
    created_at = models.DateTimeField(
        verbose_name='Дата обращения',
        auto_now_add=True
    )
