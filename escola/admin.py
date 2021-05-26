from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from . models import (
    Aluno,
    ItemBiblioteca,
    SaidaDeLivro,
    Turma, Biblioteca, 
    SaidaDeLivro, 
    Livro,
    Autor,
)

# Deixar os nomes dos alunos por ordem alfabetica.

class AlunoInline(admin.TabularInline):
    model = Aluno


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome','Turma','email')
    ordering = ['nome']
    search_fields = ['nome', 'numero','bairro']
    
admin.site.register(Aluno, AlunoAdmin)
# Turma

class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ['nome']
    inlines = [
        AlunoInline,
    ]

admin.site.register(Turma, TurmaAdmin)


class ItemBibliotecaInline(admin.TabularInline):
    model = ItemBiblioteca



# Biblioteca.

class BibliotecaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ['nome']
    inlines = [
        ItemBibliotecaInline,
    ]

admin.site.register(Biblioteca, BibliotecaAdmin)


# Saida de Livro.

class SaidaDeLivroAdmin(admin.ModelAdmin):
    list_display = ('Biblioteca', 'Aluno', 'saida', 'entrega')

admin.site.register(SaidaDeLivro, SaidaDeLivroAdmin)   

# Livros

class LivroAdmin(admin.ModelAdmin):
    pass 
admin.site.register(Livro, LivroAdmin)

# Autor

class AutorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Autor, AutorAdmin)

