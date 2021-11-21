from django.db import models
from django.db.models.base import Model
from django.urls import reverse

class Artista(models.Model):
    nombre_artista = models.CharField('Nombre',max_length=100)
    pais = models.CharField('País',max_length=50, blank=True)

    def __str__(self):
        return self.nombre_artista

class Discografica(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    email = models.EmailField('Email', max_length=100,blank=True)

    def __str__(self):
        return self.nombre

class Album(models.Model):
    FORMATOS = (
        ('VNL', 'Vinilo'),
        ('CD', 'Compact Disc'),
        ('CST', 'Cassette'),
    )
    artistas = models.ManyToManyField(Artista)
    titulo = models.CharField('Título album',max_length=100)
    fecha_salida = models.DateField('Fecha de salida', blank=True, auto_now_add=True)
    formato = models.CharField(max_length=3, choices=FORMATOS)
    genero = models.CharField('Género', max_length=200, blank=True)
    discografica = models.ForeignKey(Discografica, on_delete=models.SET_NULL, null=True, verbose_name='Discográfica')
    duracion = models.DecimalField('Duración total',max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.titulo

    def get_artistas(self):
        return "\n".join([a.nombre_artista for a in self.artistas.all()])
    

class Cancion(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    duracion = models.DecimalField('Duración',max_digits=6, decimal_places=2, blank=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre

