from django.contrib import admin
from django.db.models import fields

# Register your models here.
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
    list_display = ['titulo','formato','get_artistas','cover']
    list_filter = ['discografica','genero']