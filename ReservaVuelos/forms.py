from django import forms
from .models import Login, Vuelo, RegUsuario
from django.contrib.auth.models import User

class FormularioLogin(forms.Form):
    class Meta:
        model = Login
        fields = ["username", "password"]

class FormularioRegistro(forms.Form):
    Nombre = forms.CharField(max_length=100)
    Apellido = forms.CharField(max_length=100)
    username = forms.CharField(max_length=40)
    email = forms.EmailField()
    password = forms.CharField(max_length=20)
    password2 = forms.CharField(max_length=20)
    """class Meta:
        model = Registro
        fields = ["Nombre","Apellido","Nombre_de_usuario","Email","Password","Password2"]"""

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de Usuario ya registrado')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Este Email ya esta registrado')
        return email

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las Contraseñas no coinciden')
        return password2

class FormularioVuelo(forms.Form):
    origen = forms.CharField(max_length=200)
    destino = forms.CharField(max_length=200)
    partida = forms.DateField()
    regreso = forms.DateField()
    clase = forms.CharField(max_length=50)
    tipo = forms.CharField(max_length=20)
    adulto = forms.IntegerField()
    niño = forms.IntegerField()
    bebe = forms.IntegerField()
    tarifa = forms.DecimalField(max_digits=10, decimal_places=2)
    """def clean_origen(self):
        v_origen = self.cleaned_data
        org = v_origen.get('origen')
        if org.isalpha() != True:
            raise forms.ValidationError("Este es un campo de solo letras")
        return org
    def clean_destino(self):
        v_destino = self.cleaned_data
        dest = v_destino.get('destino')
        if dest.isalpha() != True:
            raise forms.ValidationError("Este es un campo de solo letras")
        return dest
    def clean_clase(self):
        v_clase = self.cleaned_data
        clas = v_clase.get('clase')
        if clas.isalpha() != True:
            raise forms.ValidationError("Este es un campo de solo letras")
        return clas
    def clean_tipo(self):
        v_tipo = self.cleaned_data
        tip = v_tipo.get('tipo')
        if tip.isalpha() != True:
            raise forms.ValidationError("Este es un campo de solo letras")
        return tip"""
