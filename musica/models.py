from django.db import models
from django.db.models.base import Model
from django.urls import reverse
from django.conf import settings


class Artista(models.Model):
    nombre_artista = models.CharField('Nombre',max_length=100)
    pais = models.CharField('País',max_length=50, blank=True)

    def __str__(self):
        return self.nombre_artista

    def get_absolute_url(self):
        return reverse('artista_detalle', args=[str(self.id)])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artistas'] = Artista.objects.all() 
        return context

class Discografica(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    email = models.EmailField('Email', max_length=100,blank=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('discografica_detalle', args=[str(self.id)])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['discograficas'] = Discografica.objects.all() 
        return context

class Album(models.Model):
    FORMATOS = (
        ('VNL', 'Vinilo'),
        ('CD', 'Compact Disc'),
        ('CST', 'Cassette'),
    )
    GENEROS = (
        ('ROCK', 'Rock&Roll'),
        ('POP', 'Pop'),
        ('CLAS', 'Clásica'),
        ('RNB', 'Rhythm and Blues'),
        ('DISC', 'Disco'),
        ('COUN', 'Country'),
        ('JAZZ', 'Jazz'),
        ('REGG', 'Reggae'),
        ('FLAM', 'Flamenco'),
        ('BSO', 'Bandas Sonoras'),
        ('BAL', 'Baladas'),
    )
    artistas = models.ManyToManyField(Artista)
    titulo = models.CharField('Título album',max_length=100)
    formato = models.CharField(max_length=3, choices=FORMATOS)
    genero = models.CharField(max_length=4, choices=GENEROS)
    discografica = models.ForeignKey(Discografica, on_delete=models.SET_NULL, null=True, verbose_name='Discográfica')
    duracion = models.DecimalField('Duración total',max_digits=6, decimal_places=2, default=0.00)
    cover = models.ImageField(default="imagenes/not-found.png",upload_to="imagenes/", blank=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('album_detalle', kwargs={'pk': self.pk})

    def get_artistas(self):
        return "\n".join([a.nombre_artista for a in self.artistas.all()])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all() 
        return context

    class Meta:
        verbose_name = 'Album'

class Cancion(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    duracion = models.DecimalField('Duración',max_digits=6, decimal_places=2, blank=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('cancion_detalle', args=[str(self.id)])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['canciones'] = Cancion.objects.all() 
        return context
    
    def get_genero(self):
        return "\n".join([a.genero for a in self.album()])

def get_upload_to(instancia, filename):
    return instancia.get_upload_to(filename)

class Imagen(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='título')
    file = models.ImageField(upload_to="imagenes", verbose_name='imagen',
        height_field= 'alto', width_field='ancho')
    ancho = models.IntegerField(editable=False, default=0)
    alto = models.IntegerField(editable=False, default=0)
    fecha_subida = models.DateTimeField(verbose_name='Fecha de subida', auto_now_add=True,
        db_index=True, blank=True, null=True)
    subida_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Subida por usuario',
        null=True, blank=True, editable=False, 
        on_delete=models.SET_NULL
    )
    
    def __str__(self):
        return self.titulo
