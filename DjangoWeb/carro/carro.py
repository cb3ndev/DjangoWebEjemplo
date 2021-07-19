class Carro: #Crearemos la clase para el carro para que funcione la logica de nuestro carro 
	def __init__(self, request):
		self.request=request #Carro tiene dos campos de clase request y session,
		self.session=request.session #siendo session un diccionario
		carro=self.session.get("carro") #get es una función para los diccionarios
										# la variable carro sera un diccionario que habra obtenido de otro diccionario (self.session) cuyo
										# uno de sus elementos clave es "carro", esto es lo que obtiene con get: el valor(un diccionario 
										#cuyos elementos clave son ids de los productos y sus valores son: precios,imagen, etc.) 
										# cuya clave es la palabra "carro"
		if not carro: #En caso de que no hya carro (variable carro esta vacía) pues creamos el diccionario pero vacio
			carro=self.session["carro"]={}
		#else:  #NOTA el comnetario de la linea sigte es anterior, se comento el else y su instruccion siempre es leida, esto debido a un error
		self.carro=carro #Si al iniciar una nueva sesion hay un carro que ya existia pues justo lo que queremos es que
						 # no se pierda sus productos pues eso mismo le asignamos a este carro el carro que ya existe


	def agregar(self, producto): #Funcion para agregar productos
		if (str(producto.id) not in  self.carro.keys()): #Aqui consultamos si el prodcuto que keremos agregar NO esta ya en el carro 
														#esto lo hacemos por medio del id
			self.carro[producto.id]={ #Aqui como un valor del diccionario carro agregamos el id del producto (del producto agregado por 
									#medio de la funcion)y a continuación agregamos un diccionario. Tal como lo dijimos mas arriba
				"producto_id":producto.id,
				"nombre":producto.nombre,
				"precio":str(producto.precio), #debemos convertior a string el precio 
				"cantidad":1, #Esto lo hace si no hay este producto en el carro, en el caso de que haya debe aumentarse esta cantidad
							  #eso lo haremos despues
				"imagen":producto.imagen.url
			}
		else:
			for key, value in self.carro.items(): #En aqui se recorre los elementos del diccionario, por ejemplo en el primer loop
												  # key toma el valor del primer elemento clave ("producto_id") y value, del valor de esa clave
												  #(producto.id) En el segundo loop "nombre" y producto.nombre y asi hasta terminar todos los elementos del dict

				if key==str(producto.id): #Vamos recorriendo todos los elementos del dict carro hasta que key coincida con el producto repetido
					value["cantidad"]=value["cantidad"]+1 #cuando coincida sumamos en uno la cantidad
					break #Esto se pone para deternse cuando YA se haya dado la coincidencia para evitar desperdiciar memoria en un recorrido que ya no es util
		#Agregado por primera o n vez un producto en el carro, fuera del if llamamos una funcion para guardar 
		#el carro en la sesion, dicha funcion la definiremos mas abajo.

		self.guardar_carro()


	def guardar_carro(self):
		self.session["carro"]=self.carro #Actualizamos el carro con el nuevo carro (despues de agregar un producto por ej.)
		self.sessio:n.modified=True #Esta parte sirve para indicar que en efecto se ha modificado la session despues de agregar/quitar algun elemento al carro
	
	def eliminar(self, producto): #Esta funcion sirve para elimnar por completo un producto del carro
		producto.id=str(producto.id)
		if producto.id in self.carro:
			del self.carro[producto.id] #Borramos con del ese producto por medio de su id, por mas que haya 100 unidades de ese producto se borraran todos
			self.guardar_carro()

	def restar_producto(self,producto): #Funcion contraria a agregar, aca sin embargo siempre se quitaran cosas cuando ya existan
		for key, value in self.carro.items():
			if key==str(producto.id):
				value["cantidad"]=value["cantidad"]-1
				if value["cantidad"]<1: #Despues de eliminar un  producto resulta que es menor a 1, osea quedan cero producto
										#lo que se hace es eliminar el producto
					self.eliminar(producto)
				break
		self.guardar_carro()

	def limpiar_carro(self): #Un reset del carro, simplemente regresamos el carro al valor inicial
		carro=self.session["carro"]={}
		self.session.modified=True


