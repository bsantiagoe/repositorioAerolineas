from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.inicio),
    url(r'^nuevoUsuario/$', views.nuevoUsuario),
    url(r'^Vista/$', views.Vista),
    url(r'^comprar/$', views.comprar),
    url(r'^consultar/$', views.consultar),
    url(r'^reservar/$', views.reservar),
    url(r'^crearVuelo/$', views.crearVuelo),
    url(r'^eliminar/$', views.eliminar),
    url(r'^eliminarV/$', views.eliminarV),
    url(r'^modificar/$', views.modificar),
    url(r'^salir/$', views.salir),
    url(r'^list/$', views.list),
]
