from django.shortcuts import render
from .forms import forms


from .forms import ContatoForm




def index(request):

    context = {
        'welcome' : 'Welcome to KemSoftware',
        'begin' : 'Starting my first page By Kemuel Kesley'
    }

    return render(request, 'index.html', context)



def contato(request):
    
    form = ContatoForm

    context = {
        'form':form
    }

    return render(request, 'contato.html', context)   

<<<<<<< HEAD

# Create your views here.

def index(request):

    context = {
        'welcome' : 'Welcome KemSoftware',
        'begin' : 'Starting my first page By Kemuel Kesley'
    }

    return render(request, 'index.html', context)
=======
>>>>>>> 9c92ed488404521468c1f02609c30e47dd369506
