from django.shortcuts import render
from django.http import HttpResponse


def Empresa(request):
    return render (request, "paginas/empresa.html")