#eSTA APP se hizo despues de la prinicpal proyectoweb ver esa primero

from django.db import models

# Create your models here.
class Servicio(models.Model):
	titulo=models.CharField(max_length=50)
	contenido=models.CharField(max_length=50)
	imagen=models.ImageField(upload_to="servicios") #Si dejamos sin argumentos este campo la imagen sera guardada por defecto en afuera del proyecto, para ordenar mejor n8uestros archivos, ponemos el argumento
	#upload_to="servicios", asi creara una carpeta llamada servicios dentro de la carpeta media y los guardara ahi, tener en cuenhta que para esto debe haberse indicado correctamente la existencia de la carpeta media en settings 
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now_add=True)

#La clase meta segun la docuemntación es "todo lo que no es un campo" es data sobre este modelo que se encuentra fuera del modelo, por ejemplo: el nombre verbose que saldr
#en el adminisgtareción, nombres de las tablas de la bd, etc etc
	class Meta:
		verbose_name='servicio'
		verbose_name_plural='servicios'


	def __str__(self):
		return self.titulo
