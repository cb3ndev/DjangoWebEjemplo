#eSTA APP se hizo despues de la prinicpal proyectoweb ver esa primero
from django.urls import path

from . import views



urlpatterns = [

    
    path('', views.servicios, name="Servicios"),
    

]
