from django.shortcuts import render
from django.http import HttpResponse

def inicio (request):
    return HttpResponse ("<h1>Inicio</h1>)")

def Empresa(request):
    return render (request, "paginas/empresa.html")