# Generated by Django 3.2.3 on 2021-05-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0011_auto_20210521_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='geral',
            name='escolha_informacoes',
            field=models.CharField(choices=[('INI', 'Iniciante'), ('JU', 'Junior'), ('SE', 'Senior'), ('GR', 'Graduado')], default='INI', max_length=3),
        ),
    ]
