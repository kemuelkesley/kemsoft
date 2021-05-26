# Generated by Django 3.2.3 on 2021-05-23 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0021_auto_20210523_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='biblioteca',
            name='Turma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='escola.turma'),
        ),
        migrations.AlterField(
            model_name='biblioteca',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descição do Livro'),
        ),
    ]
