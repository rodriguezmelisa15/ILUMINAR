from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Empresas, Sucursales


def Empresa(request):
    return render (request, "paginas/empresa.html")


def Sucursal(request):
    sucursales = Sucursales.objects.all().values()
    context = {
        'sucursales': sucursales,
    }
    return render(request, 'paginas/sucursales.html', context)

def Usuario (request):
    return render (request, "paginas/login.html")




