from django import forms


# Criar formulario

class ContatoForm(forms.Form):
    nome = forms.CharField(initial='Seu nome completo',max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    celular = forms.CharField(label='Celular',initial='Digite os números sem espaços', max_length=11)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)