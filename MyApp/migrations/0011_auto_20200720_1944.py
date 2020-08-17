# Generated by Django 3.0.6 on 2020-07-20 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0010_auto_20200705_1611'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicedurationmodel',
            options={'verbose_name': 'Продолжительность поминовения', 'verbose_name_plural': 'Продолжительность поминовений'},
        ),
        migrations.AlterField(
            model_name='servicedurationmodel',
            name='service_duration_value',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Продолжительность поминовения'),
        ),
    ]