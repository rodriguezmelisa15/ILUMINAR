from django.urls import path
from . import views

urlpatterns = [
    path('Empresa', views.Empresa, name='Empresa'),
    path('sucursales/', views.Sucursal, name='sucursales'),
    path ('login/', views.Usuario, name='login'),


          
]
