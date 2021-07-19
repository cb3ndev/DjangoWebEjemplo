#from .carro import Carro


def importe_total_carro(request):#Esta funcion sirve para darnos el valor actual del carro, osea el importe que se debe paghar segun que cosas tenga el car
	total=0 #Empieza en cero
	if request.user.is_authenticated:#Verificamos la autenticidad del usuARIO ANTES (SI EL USARIO ESTA LOGGEADO)
		for key, value in request.session["carro"].items(): #Recorremos cada producto del carro
			total=total+(float(value["precio"])*value["cantidad"]) #Y hallamos su importe total y sumamos uno a uno
	return{"importe_total_carro":total} #finalmente retornamoss un diccionario con key: "importe_tyotal_carro" y valor lo que sacamos de total


#NOTA: La razon por la que creamos esta funcion con este script y todo el nombre de "context_processor" es porque queremos que el diccionario
#retornado sea como una variable global, es decir queremos que esta variable de contexto, exista en todos los views del proyecto sin tener 
#que especificarlo en cada uno como normalemnet hacemos con las variables de conetxto .
#Los prorcesadores de contexto no son lo mismo que los middleware, ver en google o youtube para mas referencia.
#Los procesadores de contexto se deben especificar en settings en la parte de templates, ver ahi para mas informacion.
	
