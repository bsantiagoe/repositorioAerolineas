from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.username

class RegUsuario(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    username = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    def __str__(self):
        return self.username

class Vuelo(models.Model):
    origen = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    partida = models.DateField()
    regreso = models.DateField()
    clase = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)
    adulto = models.IntegerField()
    niño = models.IntegerField()
    bebe = models.IntegerField()
    tarifa = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.clase

class RegCompra(models.Model):
    idU = models.ForeignKey('RegUsuario')
    idV = models.ForeignKey('Vuelo')

    def __str__(self):
        return self.idU.username
