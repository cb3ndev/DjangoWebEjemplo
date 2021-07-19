# app numro 3 en orden
#Se creo este script especificamente porque esta app requiere de formularios
from django import forms

class FormularioContacto(forms.Form):
	nombre=forms.CharField(label="Nombre", required=True)
	email=forms.CharField(label="E-mail", required=True)
	contenido=forms.CharField(label="Contenido", widget=forms.Textarea)#Com TextArea hacemos que este campo aparezca como una caja 
	#grande en el form para poner mucho texto