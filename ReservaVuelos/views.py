from django.shortcuts import render, redirect, render_to_response
from .forms import FormularioLogin, FormularioRegistro, FormularioVuelo
from .models import Login, Vuelo, RegUsuario
from django.template import RequestContext
# para hacer login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.contrib.auth.models import User
from django.db import models

import json as simplejson
import json

# Create your views here.

def inicio(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request,acceso)
                    return redirect(Vista)
                else:
                    return render_to_response('noactivo.html')
            else:
                return render_to_response('nousuario.html')
    else:
        formulario = AuthenticationForm()
        return render(request, 'inicio.html', {'formulario':formulario})

def nuevoUsuario(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST or None)
        if form.is_valid():
            #cleaned_data = form.cleaned_data
            Nombre = request.POST['Nombre']
            Apellido = request.POST['Apellido']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user_model = User.objects.create_user(username=username, password=password)
            user_model.email = email
            user_model.first_name = Nombre
            user_model.last_name = Apellido
            user_model.save()
            return redirect('/')
    else:
        form = FormularioRegistro()
    return render(request, 'nuevoUsuario.html', {'form':form})

@login_required(login_url='/')
def Vista(request):
    usuario = request.user
    context = {
        'usuario':usuario,
    }
    return render(request, 'Vista.html', context)

@login_required(login_url='/')
def crearVuelo(request):
    usuario = request.user
    f = FormularioVuelo(request.POST or None)
    if request.method == 'POST':
        if f.is_valid():
            datos = f.cleaned_data
            v = Vuelo()
            v.origen = datos.get("origen")
            v.destino = datos.get("destino")
            v.partida = datos.get("partida")
            v.regreso = datos.get("regreso")
            v.clase = datos.get("clase")
            v.tipo = datos.get("tipo")
            v.adulto = datos.get("adulto")
            v.niño = datos.get("niño")
            v.bebe = datos.get("bebe")
            v.tarifa = datos.get("tarifa")
            if v.save() != True:
                return redirect(Vista)
    context = {
        'f':f,
        'usuario':usuario,
    }
    return render(request, "crearVuelo.html", context)

@login_required(login_url='/')
def comprar(request):
    usuario = request.user
    vuelos = Vuelo.objects.all()
    context = {
        'usuario':usuario,
        'vuelos':vuelos,
    }
    return render(request, 'comprar.html', context)

@login_required(login_url='/')
def consultar(request):
    usuario = request.user
    vuelos = Vuelo.objects.all()
    context = {
        'usuario':usuario,
        'vuelos':vuelos,
    }
    return render(request, 'consultar.html', context)

@login_required(login_url='/')
def reservar(request):
    usuario = request.user
    vuelos = Vuelo.objects.all()
    context = {
        'usuario':usuario,
        'vuelos':vuelos,
    }
    return render(request, 'reservar.html', context)

@login_required(login_url='/')
def modificar(request):
    f = FormularioVuelo(request.POST or None)
    v = Vuelo.objects.get(id=request.GET['id'])

    f.fields["origen"].initial = v.origen
    f.fields["destino"].initial = v.destino
    f.fields["partida"].initial = v.partida
    f.fields["regreso"].initial = v.regreso
    f.fields["clase"].initial = v.clase
    f.fields["tipo"].initial = v.tipo
    f.fields["adulto"].initial = v.adulto
    f.fields["niño"].initial = v.niño
    f.fields["bebe"].initial = v.bebe
    f.fields["tarifa"].initial = v.tarifa

    if request.method == 'POST':
        if f.is_valid():
            datos = f.cleaned_data
            v.origen = datos.get("origen")
            v.destino = datos.get("destino")
            v.partida = datos.get("partida")
            v.regreso = datos.get("regreso")
            v.clase = datos.get("clase")
            v.tipo = datos.get("tipo")
            v.adulto = datos.get("adulto")
            v.niño = datos.get("niño")
            v.bebe = datos.get("bebe")
            v.tarifa = datos.get("tarifa")
            if v.save() != True:
                return redirect(consultar)
    context = {
        'v':v,
        'f':f,
    }
    return render(request, "modificar.html", context)

@login_required(login_url='/')
def salir(request):
    logout(request)
    return redirect('../')

@login_required(login_url='/')
def eliminar(request):
    v = Vuelo.objects.get(id=request.GET['id'])
    context = {'v':v,}
    return render(request, "eliminar.html", context)

@login_required(login_url='/')
def eliminarV(request):
    v = Vuelo.objects.get(id=request.GET['id'])
    v.delete()
    return redirect(consultar)

def list(request):
    vuelos = Vuelo.objects.all()
    vresult = []
    vreturn = {}
    for v in vuelos:
        vresult.append({"Origen":v.origen,
                        "Destino":v.destino,
                        #"Partida":v.partida,
                        #"Regreso":v.regreso,
                        "Clase":v.clase,
                        "Vuelo":v.tipo,
                        "Adultos":v.adulto,
                        "Niños":v.niño,
                        "Bebes":v.bebe,
                        #"Tarifa":v.tarifa,
                        })
    vreturn['Vuelo'] = vresult
    return HttpResponse(simplejson.dumps(vreturn),'application/json')
    """query = Vuelo.objects.all()
    query = serializers.serialize('json',query)
    return HttpResponse(query, 'application/json')"""
