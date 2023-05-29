from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('Empresa', views.Empresa, name='Empresa'),
          
]