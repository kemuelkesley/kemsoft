# Generated by Django 3.2.3 on 2021-05-23 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0017_biblioteca_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='biblioteca',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descição  do Livro'),
        ),
    ]
