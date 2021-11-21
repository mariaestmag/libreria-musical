"""libreria_musical URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf import settings
from django.urls import include, path
from django import urls, views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static #nos sirve las variables estáticas
from musica.views import indice, AlbumListView, AlbumDetailView, ArtistaListView,ArtistaDetailView, CancionListView, CancionDetailView, DiscograficaListView, DiscograficaDetailView
from django.contrib.auth.views import LogoutView
from libreria_musical.settings import LOGOUT_REDIRECT_URL #crearemos una vista indice para poder importarla y utilizarla en patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', indice, name ='indice'),
    path('albums/', AlbumListView.as_view(), name ='albums_lista'),
    path('album/<int:pk>', AlbumDetailView.as_view(), name='album_detalle'),
    path('artistas/', ArtistaListView.as_view(), name ='artistas_lista'),
    path('artista/<int:pk>', ArtistaDetailView.as_view(), name='artista_detalle'),
    path('canciones/', CancionListView.as_view(), name ='canciones_lista'),
    path('cancion/<int:pk>', CancionDetailView.as_view(), name='cancion_detalle'),
    path('discograficas/', DiscograficaListView.as_view(), name ='discograficas_lista'),
    path('discografica/<int:pk>', DiscograficaDetailView.as_view(), name='discografica_detalle'),
    path("logout/", LogoutView.as_view(), name="logout"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
