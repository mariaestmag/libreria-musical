from django.contrib import admin
from django.db.models import fields
from django.utils.html import format_html

from .models import Artista, Discografica, Cancion, Album

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ['nombre_artista','pais','album']
    list_filter = ['pais'] 
    search_fields = ['nombre_artista', 'album__genero']
    '''Relaciones N:M y con FK, hay que referirlas con dos barras bajas.
    Si escribo un género de álbum en la barra de Artistas, lo filtra bien'''

@admin.register(Discografica)
class DiscograficaAdmin(admin.ModelAdmin):
    list_display = ('nombre','email')
    search_fields = ['nombre']


@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ['nombre','duracion','album']
    list_filter = ['album']
    search_fields = ['nombre','album__titulo','album__genero']
    '''Relaciones N:M y con FK, hay que referirlas con dos barras bajas.
    Si escribo un género de álbum en la barra de Canciones, lo filtra bien'''


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['titulo','formato','get_artistas','cover','thumbnail']
    list_filter = ['discografica','genero']
    search_fields = ['titulo','artistas__nombre_artista']
    '''Relaciones N:M y con FK, hay que referirlas con dos barras bajas'''

    '''
    Miniatura para previsualizar imagen
    '''
    def thumbnail(self, obj):
        return format_html('<img src="{}" style="width: 70px; height: 70px"/>'.format(obj.cover.url))
    thumbnail.short_description = 'thumbnail'