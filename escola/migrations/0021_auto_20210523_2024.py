# Generated by Django 3.2.3 on 2021-05-23 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0020_auto_20210523_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biblioteca',
            name='data',
        ),
        migrations.AddField(
            model_name='biblioteca',
            name='data_entrega',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Entrega'),
        ),
        migrations.AddField(
            model_name='biblioteca',
            name='data_saida',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Saida'),
        ),
    ]
