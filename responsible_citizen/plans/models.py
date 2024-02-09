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
