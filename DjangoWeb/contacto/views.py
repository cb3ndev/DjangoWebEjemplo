#App nro 3 en orden
from django.shortcuts import render, redirect
from . forms import FormularioContacto #Esta app tiene un script forms debemos importar para hacer uso de lo que este dentro
from django.core.mail import EmailMessage #Importacion necesaria para enviar un mensaje a un correo electroniclo
# Create your views here.

def contacto(request):
	formulario_contacto=FormularioContacto() #Se crea una instancia de la clase FormularioContacto 

	if request.method=="POST": #Aqui s erescata la informacion del form
		formulario_contacto=FormularioContacto(data=request.POST) #Notar el parecido con la linea 8, aqui si hacemos referencia al request
		if formulario_contacto.is_valid(): #Validamos la data del form
			nombre=request.POST.get("nombre")
			email=request.POST.get("email")
			contenido=request.POST.get("contenido")

			#Esta parte del codigo es para enivar correos a tarves del formulario 
			email=EmailMessage("MEsaje desde app Django!!!!!!!!", #subject del corrreo
				"El usario con nombre {} con la dirección {} escribe lo sgte.: \n\n {}".format(nombre, email, contenido), #conmtenido del correo
				"",#De queine viene el correo, ya sabemos que es de la app por eso no ponemos nada
				["YYYYYYY@YYY.com"],#La cuenta HACIA donde se mandara el correo, puede ser el mismo host que se configuro (ver settings)
				#o puede ser otro correo, si es otro, lo llenado en el formulario se enviara al host y a este. Notar que el mensaje
				#se envia siempre desde el host. 
				reply_to=[email]) #En caso de que se quiera contestar el correo se hara hacia el email que se puso en el formulario

			try: #En caso haya algun error solo indicaremos valido cuando se haya enviado el email, sino que vote error a tarves del url
				#Este codigo s ehizo despues del codigo de la linea 32
				email.send()
				return redirect("/contacto/?valido")
			except:
				return redirect("/contacto/?novalido")


			#return redirect("/contacto/?valido") #Cuando en la pagina enviemos un ndato por post y se guarde en las variables
												#redireccionaremos hacia la misma pagina pero con un mensaje enviado a traves del url de "valido"
												#puede ser cualquier palabra, aca usamos "valido"
	


	return render(request,"contacto/contacto.html", {"miFormulario":formulario_contacto})