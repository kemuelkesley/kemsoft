# Generated by Django 3.2.3 on 2021-05-25 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0033_itembiblioteca_biblioteca'),
    ]

    operations = [
        migrations.AddField(
            model_name='itembiblioteca',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
    ]
