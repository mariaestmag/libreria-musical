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

def canciones_mod(request):
    lista_canciones = Cancion.objects.all() 
    context = {'canciones': lista_canciones}
    return render(request, 'canciones/listar_modificar.html', context)

def canciones_del(request):
    lista_canciones = Cancion.objects.all() 
    context = {'canciones': lista_canciones}
    return render(request, 'canciones/listar_eliminar.html', context)

def discograficas_mod(request):
    lista_discograficas = Discografica.objects.all() 
    context = {'discograficas': lista_discograficas}
    return render(request, 'discograficas/listar_modificar.html', context)

def discograficas_del(request):
    lista_discograficas = Discografica.objects.all() 
    context = {'discograficas': lista_discograficas}
    return render(request, 'discograficas/listar_eliminar.html', context)

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
    '''
    Clase para crear álbumes
    '''
    model = Album
    fields = '__all__'
    template_name = 'albums/crear.html'
    success_url = '/'
    success_message = 'Album creado correctamente'


class AlbumUpdateView(SuccessMessageMixin,UpdateView):
    '''
    Clase para modificar álbumes
    '''
    model = Album
    fields = '__all__'
    template_name = 'albums/modificar.html'
    success_url = '/'
    success_message = 'Album modificado correctamente'


class AlbumDeleteView(DeleteView):
    '''
    Clase para eliminar álbumes
    '''
    model = Album
    success_url = reverse_lazy('albums_lista')
    template_name = 'albums/eliminar.html'
    success_message = 'Album eliminado correctamente'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AlbumDeleteView, self).delete(request, *args, **kwargs)

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
    '''
    Clase para crear artistas
    '''
    model = Artista
    fields = '__all__'
    template_name = 'artistas/crear.html'
    success_url = '/'
    success_message = 'Artista creado/a correctamente'

class ArtistaUpdateView(SuccessMessageMixin,UpdateView):
    '''
    Clase para modificar artistas
    '''
    model = Artista
    fields = '__all__'
    template_name = 'artistas/modificar.html'
    success_url = '/'
    success_message = 'Artista modificado/a correctamente'

class ArtistaDeleteView(DeleteView):
    '''
    Clase para borrar artistas
    '''
    model = Artista
    success_url = reverse_lazy('artistas_lista')
    template_name = 'artistas/eliminar.html'
    success_message = 'Artista eliminado/a correctamente'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ArtistaDeleteView, self).delete(request, *args, **kwargs)

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

class CancionCreateView(SuccessMessageMixin, CreateView):
    '''
    Clase para crear canciones
    '''
    model = Cancion
    fields = '__all__'
    template_name = 'canciones/crear.html'
    success_url = '/'
    success_message = 'Cancion creada correctamente'


class CancionUpdateView(SuccessMessageMixin,UpdateView):
    '''
    Clase para modificar canciones
    '''
    model = Cancion
    fields = '__all__'
    template_name = 'canciones/modificar.html'
    success_url = '/'
    success_message = 'Canción modificada correctamente'

class CancionDeleteView(DeleteView):
    '''
    Clase para borrar canciones
    '''
    model = Cancion
    success_url = reverse_lazy('artistas_lista')
    template_name = 'canciones/eliminar.html'
    success_message = 'Canción eliminada correctamente'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CancionDeleteView, self).delete(request, *args, **kwargs)

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

class DiscograficaCreateView(SuccessMessageMixin, CreateView):
    '''
    Clase para crear discográfica
    '''
    model = Discografica
    fields = '__all__'
    template_name = 'discograficas/crear.html'
    success_url = '/'
    success_message = 'Discográfica creada correctamente'

class DiscograficaUpdateView(SuccessMessageMixin, UpdateView):
    '''
    Clase para modificar discográficas
    '''
    model = Discografica
    fields = '__all__'
    template_name = 'discograficas/modificar.html'
    success_url = '/'
    success_message = 'Discográfica modificada correctamente'

class DiscograficaDeleteView(DeleteView):
    '''
    Clase para borrar discográficas
    '''
    model = Discografica
    success_url = reverse_lazy('discograficas_lista')
    template_name = 'discograficas/eliminar.html'
    success_message = 'Discográfica eliminada correctamente'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DiscograficaDeleteView, self).delete(request, *args, **kwargs)

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

# Subida y manejo de imágenes

class ImagenesListView(ListView):
    model = Imagen
    template_name = 'imagenes/imagenes_list.html'
    context_object_name = 'imagenes'
    #paginate_by = 10
    ordering = ['-fecha_subida']

class ImagenCreateView(SuccessMessageMixin, CreateView):
    model = Imagen
    fields = '__all__'
    template_name = 'imagenes/imagen_crear.html'
    success_url = '/'
    # form_class = AuthorForm
    success_message = "%(titulo)s se ha subido correctamente"

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.subida_por = self.request.user
        return super().form_valid(form)