from django.db import models
from django.forms import ModelForm, DateInput
from musica.models import Album,Artista,Cancion,Discografica
from django import forms

class AlbumForm(ModelForm):
    '''
    Formulario para crear albums
    '''
    class Meta:
        model = Album
        fields = '__all__'

class ArtistaForm(ModelForm):
    '''
    Formulario para crear artistas
    '''
    class Meta:
        model = Artista
        fields = '__all__'

class CancionForm(ModelForm):
    '''
    Formulario para crear canciones
    '''
    class Meta:
        model = Cancion
        fields = '__all__'

class DiscograficaForm(ModelForm):
    '''
    Formulario para crear discográficas
    '''
    class Meta:
        model = Discografica
        fields = '__all__'
        
