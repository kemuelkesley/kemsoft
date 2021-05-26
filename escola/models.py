from django.contrib.admin.options import BaseModelAdmin
from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import BLANK_CHOICE_DASH, CharField, DateField
from django.utils import tree


# Classe Turma

class Turma(models.Model):
    nome = models.CharField(max_length=30, null=True, blank=True)
    def __str__ (self):
        return self.nome

# Classe Aluno

class Aluno(models.Model):
    # Cadastros dos alunos
    
    nome = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nome')
    cidade = models.CharField(max_length=50, null=True, blank=True, verbose_name='Cidade')
    bairro = models.CharField(max_length=50, null=True, blank=True, verbose_name='Bairro')
    numero = models.IntegerField(default=0, verbose_name='Número')
    email = models.EmailField(null=True, blank=True, verbose_name='E-mail')
   # idade = models.DecimalField(max_digits=2, decimal_places=2, null=True, verbose_name='Idade')
    # Foreignkey um aluno para de varios alunos para uma Turma.
    Turma = models.ForeignKey(Turma, null=True, blank=True, on_delete=models.PROTECT)
    
    def __str__ (self):
        return self.nome

# Bibliotecas


class Biblioteca(models.Model):
    nome = models.CharField(max_length=60,
    default="biblioteca central"
    )
       
    descricao = models.TextField(
       
       verbose_name ='Descrição do Livro'
    )
    def __str__(self):
        return self.nome


# Saida de Livros.

class SaidaDeLivro(models.Model):
    atendente = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='Atendente'
    )
    
    Aluno = models.ForeignKey(
        Aluno,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    
    Biblioteca = models.ForeignKey(
        Biblioteca,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    
    saida = models.DateField(
        null=True,
        verbose_name='Data de Saida'
    )
    
    entrega = models.DateField(
        null=True,
        verbose_name='Data de Entrega'
    )
    

# Autor.

class Autor(models.Model):
    nome = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Nome"
    )

    livro_autor = models.CharField(
        max_length=100,
        null=True,
        blank=True, 
        verbose_name="Livro"       
    )
    # Meta é uma classe de configuração.
    class Meta:
        verbose_name_plural="Autor"    

    def __str__ (self):
        return self.nome


# Livros

class Livro(models.Model):
    
    livro = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Livro"        
    ) 
    
    autor = models.ForeignKey(
        Autor,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name="Autor"
    )

    descricao = models.TextField(
        null=True,
        blank=True,
        verbose_name="Descrição"
    )
    
    def __str__(self):
        return self.livro 


# Item da Biblioteca

class ItemBiblioteca(models.Model):
    Livro = models.ForeignKey(
        Livro,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,        
    )
    
    quantidade = models.IntegerField(default=0)

    # descricao = models.TextField(
    #     verbose_name="Descrição"
    # )

    biblioteca = models.ForeignKey(
        Biblioteca,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,        
    )

   