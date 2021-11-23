from django.db.models.query import QuerySet
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.contrib.auth.signals import user_logged_out, user_logged_in, user_login_failed
from django.contrib import messages
from musica.forms import AlbumForm
from musica.models import *
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


def indice(request): 
    '''
    Página de indice de nuestra web
    '''
    lista_albums = Album.objects.all() 
    context = {'albums': lista_albums}
    return render(request, 'index.html', context)

def albums_mod(request):
    lista_albums = Album.objects.all() 
    context = {'albums': lista_albums}
    return render(request, 'albums/listar_modificar.html', context)

def albums_del(request):
    lista_albums = Album.objects.all() 
    context = {'albums': lista_albums}
    return render(request, 'albums/listar_eliminar.html', context)

def artistas_mod(request):
    lista_artistas = Artista.objects.all() 
    context = {'artistas': lista_artistas}
    return render(request, 'artistas/listar_modificar.html', context)

def artistas_del(request):
    lista_artistas = Artista.objects.all() 
    context = {'artistas': lista_artistas}
    return render(request, 'artistas/listar_eliminar.html', context)

# ALBUMS

class AlbumListView(ListView):
    """
    Clase genérica para listar albums
    """
    model = Album
    template_name = 'albums/listar.html'
    #paginate_by = 5
    context_object_name = "albums"    

class AlbumDetailView(DetailView):
    """
    Clase genérica para listar detalle en albums
    """
    model = Album
    template_name = 'albums/detalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all() 
        return context

class AlbumCreateView(SuccessMessageMixin, CreateView):
    model = Album
    fields = '__all__'
    template_name = 'albums/crear.html'
    success_url = '/'

class AlbumUpdateView(UpdateView):
    model = Album
    fields = '__all__'
    template_name = 'albums/modificar.html'
    success_url = '/'

class AlbumDeleteView(SuccessMessageMixin,DeleteView):
    model = Album
    success_url = reverse_lazy('albums_lista')
    template_name = 'albums/eliminar.html'

# ARTISTAS

class ArtistaListView(ListView):
    """
    Clase genérica para listar artistas
    """
    model = Artista
    template_name = 'artistas/listar.html'
    #paginate_by = 5
    context_object_name = "artistas"

class ArtistaDetailView(DetailView):
    """
    Clase genérica para listar detalle en artistas
    """
    model = Artista
    template_name = 'artistas/detalle.html'

class ArtistaCreateView(SuccessMessageMixin, CreateView):
    model = Artista
    fields = '__all__'
    template_name = 'artistas/crear.html'
    success_url = '/'

class ArtistaUpdateView(UpdateView):
    model = Artista
    fields = '__all__'
    template_name = 'artistas/modificar.html'
    success_url = '/'

class ArtistaDeleteView(SuccessMessageMixin,DeleteView):
    model = Artista
    success_url = reverse_lazy('artistas_lista')
    template_name = 'artistas/eliminar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artistas'] = Artista.objects.all() 
        return context

# CANCIONES

class CancionListView(ListView):
    """
    Clase genérica para listar canciones
    """
    model = Cancion
    template_name = 'canciones/listar.html'
    #paginate_by = 5
    context_object_name = "canciones"

class CancionDetailView(DetailView):
    """
    Clase genérica para listar detalle en canciones
    """
    model = Cancion
    template_name = 'canciones/detalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['canciones'] = Cancion.objects.all() 
        return context

# DISCOGRAFICAS

class DiscograficaListView(ListView):
    """
    Clase genérica para listar discográficas
    """
    model = Discografica
    template_name = 'discograficas/listar.html'
    #paginate_by = 5
    context_object_name = "discograficas"

class DiscograficaDetailView(DetailView):
    """
    Clase genérica para listar detalle en discográficas
    """
    model = Discografica
    template_name = 'discograficas/detalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['discograficas'] = Discografica.objects.all() 
        return context

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