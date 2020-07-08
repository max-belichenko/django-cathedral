# Generated by Django 3.0.6 on 2020-07-04 11:45

import MyApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0007_auto_20200704_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventphotomodel',
            name='thumbnail',
            field=models.ImageField(blank=True, help_text='Формируется автоматически из оригинального изображения', upload_to=MyApp.models.event_photo_path, verbose_name='Уменьшенное изображение'),
        ),
        migrations.AlterField(
            model_name='eventphotomodel',
            name='small_photo',
            field=models.ImageField(blank=True, help_text='Формируется автоматически из оригинального изображения', upload_to=MyApp.models.event_photo_path, verbose_name='Уменьшенное изображение'),
        ),
    ]
