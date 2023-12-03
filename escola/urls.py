<<<<<<< HEAD
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
=======
from os import name
from django.urls import path
from .views import index, contato

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato')
>>>>>>> 9c92ed488404521468c1f02609c30e47dd369506
]