from django.shortcuts import render
 #importamos la clase Servicio de models, pero de models de la app servicio, no de esta app
# Create your views here.

def home(request):
	return render(request,"ProyectoWebApp/home.html")





