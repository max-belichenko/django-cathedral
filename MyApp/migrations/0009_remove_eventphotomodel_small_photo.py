# Generated by Django 3.0.6 on 2020-07-04 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0008_auto_20200704_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventphotomodel',
            name='small_photo',
        ),
    ]
