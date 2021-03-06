# Generated by Django 3.2.4 on 2021-06-23 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0042_saidadelivro_atendente'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(blank=True, default='Números juntos', max_length=14, null=True, verbose_name='CPF'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='endereco',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Endereço'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='numero_celular',
            field=models.CharField(blank=True, default='82', max_length=12, null=True, verbose_name='Celular'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='numero_telefone',
            field=models.CharField(blank=True, default='82', max_length=11, null=True, verbose_name='Telefone'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='rg',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='RG'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='sexo',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('N', 'Opção não informada.')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='email',
            field=models.EmailField(blank=True, default='exemplo@exemplo.com.br', max_length=254, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='nome',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome'),
        ),
    ]
