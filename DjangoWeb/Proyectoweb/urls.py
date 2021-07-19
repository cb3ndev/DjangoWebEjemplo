"""Proyectoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('ProyectoWebApp/',include('ProyectoWebApp.urls')), #Aqui se enlaza hacia el urls de otras aplicaciones apps. Ahora las url de la app tendran la forma: http://127.0.0.1:8000/ProyectoWebApp/XXXXXXXX
    path('',include('ProyectoWebApp.urls')),#Si lo hacemos de esta forma, las urls quedaran de la forma normal http://127.0.0.1:8000/XXXXXXX

    path('servicios/', include('servicios.urls')), #registramos la url de nuestra app servicios igual que arriba
    path('contacto/', include('contacto.urls')),
    path('blog/', include('blog.urls')),
    path('tienda/', include('tienda.urls')),
    path('carro/', include('carro.urls')),
]
