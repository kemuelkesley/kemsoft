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
   
    SEXO_CHOICE =[ 
       ('M', 'Masculino'),
       ('F', 'Feminino'),
       ('N', 'Opção não informada.')
   ] 
    
    nome = models.CharField(max_length=50, null=True, blank=True, verbose_name='Nome')
    
    sexo = models.CharField(max_length=2, choices=SEXO_CHOICE, blank=True, null=True)
    
    cpf = models.CharField(max_length=11, blank=True, null=True, verbose_name='CPF')
    
    rg = models.CharField(max_length=13, blank=True, null=True, verbose_name='RG')
    
    cidade = models.CharField(max_length=50, null=True, blank=True, verbose_name='Cidade')
    
    bairro = models.CharField(max_length=50, null=True, blank=True, verbose_name='Bairro')
    
    endereco = models.CharField(max_length=40, blank=True, null=True, verbose_name='Endereço')
        
    numero = models.IntegerField(default=0, verbose_name='Número')
    
    numero_celular = models.CharField(max_length=12, default='82', blank=True, null=True, verbose_name='Celular')
    
    numero_telefone = models.CharField(max_length=11, default='82', blank=True, null=True, verbose_name='Telefone')
    
    email = models.EmailField(default='exemplo@exemplo.com.br',null=True, blank=True, verbose_name='E-mail')
    
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


# Calsse Atendende

class Atendente(models.Model):
    nome_atendente = models.CharField(max_length=50, blank=False, null=False, verbose_name="Nome do Atendente")

    def __str__(self):
        return self.nome_atendente




# Saida de Livros.

class SaidaDeLivro(models.Model):

    Atendente = models.ForeignKey(Atendente, blank=True ,null=True, on_delete=models.PROTECT)
   
    
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
        on_delete=models.PROTECT,        
    )
    
    quantidade = models.IntegerField(default=0)

    # descricao = models.TextField(
    #     verbose_name="Descrição"
    # )

    biblioteca = models.ForeignKey(
        Biblioteca,
        null=True,
        blank=True,
        on_delete=models.PROTECT,        
    )

