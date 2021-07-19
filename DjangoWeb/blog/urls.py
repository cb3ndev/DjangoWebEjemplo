#eSTA APP se hizo despues de la prinicpal proyectoweb ver esa primero
from django.urls import path

from . import views



urlpatterns = [

    
    path('', views.blog, name="Blog"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria") #Aca creamos una url dinamica que llama al id de losw objetos tipo categoria
    #la logica de dicho URL se encuentra en la funcion categoria de views.py, al poner el url categoria/4/ por ej, le dara el valor 4 a la variable categoria_id
    #lo que servira en views, ver views la funcion categoria para entender
    

]
