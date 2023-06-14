from django.shortcuts import render,redirect
from .models import Empresas, Sucursales,Usuarios,Articulos
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from .forms import LoginForm

def Empresa(request):
    empresas = Empresas.objects.values_list('fantasia', flat=True)
    sucursales = Sucursales.objects.values_list('direccion', flat=True)
    return render(request, 'paginas/sucursales.html', {'empresas': empresas, 'sucursales': sucursales})


def Usuario(request):
    if request.method == 'POST':
        form = LoginForm(request.POST) 
        if form.is_valid(): # se verifica si los datos ingresados en loguinform son validos
            usuario = form.cleaned_data['usuario']
            passd = form.cleaned_data['passd']
            user = authenticate(request, username=usuario, password=passd)
            if user is not None:
                login(request, user)
                return redirect('empresas')
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'paginas/login.html', {'form': form})



def Articulo(request):
    articulos = Articulos.objects.values('articulo', 'descrip', 'precio1')
    return render(request, 'paginas/articulos.html', {'articulos': articulos})