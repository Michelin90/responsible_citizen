# Generated by Django 4.2.7 on 2024-02-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0003_urgentmessage_plan_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urgentmessage',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='urgent_messages/images', verbose_name='Изображение к сообщению'),
        ),
    ]
