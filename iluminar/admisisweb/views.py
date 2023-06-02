from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Empresas, Sucursales,Usuarios
from django.contrib.auth.hashers import check_password
from django.contrib import messages


def Sucursal(request):
    empresas = Empresas.objects.all()
    sucursales = Sucursales.objects.none()  # Inicialmente, no hay sucursales seleccionadas

    if 'empresa' in request.GET:
        empresa_seleccionada_id = request.GET['empresa']
        sucursales = Sucursales.objects.filter(idemp=empresa_seleccionada_id)

    return render(request, 'paginas/sucursales.html', {'empresas': empresas, 'sucursales': sucursales})



def Usuario(request):
    return render(request, 'paginas/login.html')