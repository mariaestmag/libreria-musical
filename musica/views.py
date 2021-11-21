from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.signals import user_logged_out, user_logged_in, user_login_failed
from django.contrib import messages

from musica.models import *

def indice(request): 
    '''
    Página de indice de nuestra web
    '''
    lista_albums = Album.objects.all() 

    context = {'albums': lista_albums}

    return render(request, 'index.html', context)

# ALBUMS

def listar_albums(request): 
    '''
    Página de listar albums de nuestra web
    '''
    lista_albums = Album.objects.all() 

    context = {'albums': lista_albums}

    return render(request, 'albums/listar.html', context)

# ARTISTAS

def listar_artistas(request): 
    '''
    Página de listar artistas de nuestra web
    '''
    lista_artistas = Artista.objects.all() 

    context = {'artistas': lista_artistas}

    return render(request, 'artistas/listar.html', context)

# CANCIONES

def listar_canciones(request): 
    '''
    Página de listar canciones de nuestra web
    '''
    lista_canciones = Cancion.objects.all() 

    context = {'canciones': lista_canciones}

    return render(request, 'canciones/listar.html', context)

# DISCOGRAFICAS

def listar_discograficas(request): 
    '''
    Página de listar discograficas de nuestra web
    '''
    lista_discograficas = Discografica.objects.all() 

    context = {'discograficas': lista_discograficas}

    return render(request, 'discograficas/listar.html', context)

# Mensajes para LOGIN/LOGOUT

def mensaje_cierre(sender, user, request, **kwargs):
    messages.info(request, 'Cierre de sesión correcto.')
user_logged_out.connect(mensaje_cierre)

def mensaje_entrar(sender, user, request, **kwargs):
    messages.info(request, 'Inicio de sesión correcto.')
user_logged_in.connect(mensaje_entrar)

def mensaje_entrar(sender, user, request, **kwargs):
    messages.info(request, 'Fallo en inicio de sesión. Inténtelo de nuevo.')
user_login_failed.connect(mensaje_entrar)