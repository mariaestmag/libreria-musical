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
        
