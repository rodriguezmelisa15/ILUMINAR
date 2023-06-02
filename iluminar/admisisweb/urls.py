from django.urls import path
from . import views

urlpatterns = [
    path('sucursales/', views.Sucursal, name='sucursales'),
    path ('', views.Usuario, name='login'),


          
]