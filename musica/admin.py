from django.contrib import admin
from django.db.models import fields
from django.utils.html import format_html

from .models import Artista, Discografica, Cancion, Album

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ['nombre_artista','pais']
    list_filter = ['pais'] 

@admin.register(Discografica)
class DiscograficaAdmin(admin.ModelAdmin):
    list_display = ('nombre','email')

@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ['nombre','duracion','album']
    list_filter = ['album']

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['titulo','formato','get_artistas','cover','thumbnail']
    list_filter = ['discografica','genero']

    '''
    Miniatura para previsualizar imagen
    '''
    def thumbnail(self, obj):
        return format_html('<img src="{}" style="width: 70px; height: 70px"/>'.format(obj.cover.url))
    thumbnail.short_description = 'thumbnail'