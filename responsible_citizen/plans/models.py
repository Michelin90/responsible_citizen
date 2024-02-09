from django.db import models


class Plan(models.Model):
    """План благоустройства."""

    PLANNING = 'PLANNING'
    DESIGNING = 'DESIGNING'
    REALISATION = 'REALISATION'
    STAGE_CHOICES = [
        (PLANNING, 'Планирование'),
        (DESIGNING, 'Проектирование'),
        (REALISATION, 'Реализация')
    ]
    description = models.TextField(
        verbose_name='Описание плана благоустройства'
    )
    image = models.ImageField(
        verbose_name='Изображене плана благоустройства',
        upload_to='plans/images',
        default=None,
        null=True
    )
    stage = models.CharField(
        verbose_name='Стадия',
        max_length=11,
        choices=STAGE_CHOICES,
        default=PLANNING
    )
    pdf_file = models.FileField(
        verbose_name='Файл с подробным описанием плана благоустройства',
        upload_to='plans/pdf_files',
        default=None,
        null=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )


class UrgentMessage(models.Model):
    """Срочное сообщение."""

    description = models.TextField(verbose_name='Текст сообщения')
    image = models.ImageField(
        verbose_name='Изображение к сообщению',
        upload_to='urgent_messages/images',
        default=None,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
