#eSTA APP se hizo como el nro4
from django.urls import path

from . import views



urlpatterns = [

    
    path('', views.tienda, name="Tienda"),
    

]
