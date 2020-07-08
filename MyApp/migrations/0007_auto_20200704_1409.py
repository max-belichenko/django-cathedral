# Generated by Django 3.0.6 on 2020-07-04 11:09

import MyApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0006_auto_20200703_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventphotomodel',
            name='photo',
            field=models.ImageField(upload_to=MyApp.models.event_photo_path, verbose_name='Оригинальное изображение'),
        ),
        migrations.AlterField(
            model_name='eventphotomodel',
            name='small_photo',
            field=models.ImageField(blank=True, help_text='Формируется автоматически из оригинального изображения', upload_to='', verbose_name='Уменьшенное изображение'),
        ),
    ]
