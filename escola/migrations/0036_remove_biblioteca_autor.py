# Generated by Django 3.2.3 on 2021-05-25 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0035_auto_20210525_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biblioteca',
            name='autor',
        ),
    ]
