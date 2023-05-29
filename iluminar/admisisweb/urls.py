from django.urls import path
from . import views

urlpatterns = [
    path('Empresa', views.Empresa, name='Empresa'),
          
]