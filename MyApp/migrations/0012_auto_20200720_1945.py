# Generated by Django 3.0.6 on 2020-07-20 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0011_auto_20200720_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notemodel',
            name='delivery_dt',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Дата доставки записки по e-mail'),
        ),
        migrations.AlterField(
            model_name='notemodel',
            name='pay_dt',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Дата оплаты'),
        ),
    ]
