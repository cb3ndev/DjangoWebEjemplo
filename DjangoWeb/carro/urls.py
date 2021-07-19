#
from django.urls import path

from . import views

app_name="carro" #Esto sirve para evitar confusiones conj otras apps que pudieran tener
# el mismo nombre de paths, entonces si queremos usar el path de agregar podemos poner por ejemplo "carro:agregar"
#ver tienda.html para ver como se usa esto

urlpatterns = [

    #Agregamos las url correpsondientes a las views
    path('agregar/<int:producto_id>/', views.agregar_producto, name="agregar"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="eliminar"),
    path('restar/<int:producto_id>/', views.restar_producto, name="restar"),
    path('limpiar/', views.limpiar_producto, name="limpiar"),
    

]
