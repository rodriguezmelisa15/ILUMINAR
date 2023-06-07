from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Empresas, Sucursales,Usuarios,Articulos
from django.contrib.auth.hashers import check_password
from django.contrib import messages


def Empresa(request):
    empresas = Empresas.objects.values_list('fantasia', flat=True)
    sucursales = Sucursales.objects.values_list('direccion', flat=True)
    return render(request, 'paginas/sucursales.html', {'empresas': empresas, 'sucursales': sucursales})

def Usuario(request):
    return render(request, 'paginas/login.html')

def Articulo(request):
    articulos = Articulos.objects.values('articulo', 'descrip', 'precio1')
    return render(request, 'paginas/articulos.html', {'articulos': articulos})