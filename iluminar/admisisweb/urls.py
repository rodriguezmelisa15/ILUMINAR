from django.urls import path
from . import views

urlpatterns = [
    path('empresas/', views.Empresa, name='empresas'),
    path ('', views.Usuario, name='login'),
    path ('articulos/', views.Articulo, name='articulos'),



          
]