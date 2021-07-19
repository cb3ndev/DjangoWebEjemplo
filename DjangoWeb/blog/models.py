#eSTA APP se hizo despues de la prinicpal proyectoweb y despues de servicios. ver esas primero
from django.db import models

from django.contrib.auth.models import User #Para usar el campo usuario debemos importar esto

# Create your models here.


class Categoria(models.Model):
	nombre=models.CharField(max_length=50) 
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now_add=True)
	

	class Meta:
		verbose_name='categoria'
		verbose_name_plural='categorias'


	def __str__(self):
		return self.nombre


class Post(models.Model):

	titulo=models.CharField(max_length=50)
	contenido=models.CharField(max_length=50)
	imagen=models.ImageField(upload_to="blog", null=True, blank =True)#En un blog a diferencia de servicio, la imagen es opcional por eso se pone null=blank=True
	
	#Al momento de crear el autor entender que un autor puede crear varios posts por lo que la relacion es de uno a varios
	#A parte qyueremos que al eliminar un autor(un usuario) se borren todos sus posts en aqui usaremos una eliminacion en cascada
	autor=models.ForeignKey(User, on_delete=models.CASCADE)
	#Una categoria puede estar enn vaerios posts y un post puede tener varias categorias, es una relacion de muchos A MUCHOS (entre la clase Post y Categoria)
	categorias=models.ManyToManyField(Categoria)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now_add=True)


	class Meta:
		verbose_name='post'
		verbose_name_plural='posts'


	def __str__(self):
		return self.titulo
