from django.contrib import admin
from .models import Login, Vuelo

# Register your models here.

class AdminUsuario(admin.ModelAdmin):
    list_display = ["__str__", "username", "password"]
    class Meta:
        model = Login
admin.site.register(Login, AdminUsuario)

class AdminVuelo(admin.ModelAdmin):
    list_display = ["__str__", "origen", "destino", "partida", "regreso", "clase", "tipo", "adulto", "niño", "bebe", "tarifa"]
    class Meta:
        model = Vuelo
admin.site.register(Vuelo, AdminVuelo)
