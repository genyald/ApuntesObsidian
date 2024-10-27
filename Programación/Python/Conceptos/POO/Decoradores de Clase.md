#Python #Decoradores #Clases 

Los decoradores de clases son muy similares a los [[Decoradores|Decoradores de una funcion]], a diferencia que un decorador de clase nos permite modificar de manera programatica nuestra clase.

Para hacer uso de decoradores utilizamos `@decorador_clase`

```python
# Va a recibir como argumento una clase completa
def decorador_repr(cls):
	print('Se ejecuta decorador')
	print('Recibimos el objeto de clase:', cls.__name__)

@decorador_repr
class Persona:
	def __init__(self, nombre, apellido):
		print('Se ejecuta el inicializado')
		self._nombre = nombre
		self._apellido = apellido
		
	@property
	def nombre(self):
		return self._nombre
	@property
	def apellido(self):
		return self._apellido
	
perona1 = Persona('Juan', 'Perez')
```

Como se puede apreciar, el decorador debe regresar el objeto ya modificado, por lo que es importante que si no la modificamos por lo menos la regresamos. Si si lo hacemos debemos hacer uso de dos funciones anidadas, la cual la segunda regresa la funciona modificada:

```python
# Va a recibir como argumento una clase completa
def decorador_repr(cls):
	print('Se ejecuta decorador')
	print('Recibimos el objeto de clase:', cls.__name__)
	return cls

@decorador_repr
class Persona:
	def __init__(self, nombre, apellido):
		print('Se ejecuta el inicializado')
		self._nombre = nombre
		self._apellido = apellido
		
	@property
	def nombre(self):
		return self._nombre
	@property
	def apellido(self):
		return self._apellido
	
perona1 = Persona('Juan', 'Perez')
```

Con el uso de esto podemos modificar dinamicamente, por ejemplo el  `__repr__` de cada clase, con el metodo `__vars__` recuperamos los atributos de nuestra clase:

```python
def decorador_repr(cls):
	print('Se ejecuta decorador')
	print('Recibimos el objeto de clase:', cls.__name__)
	
	# Revisamos los atributos de clase con el metodo vars
	atributos = dict(vars(cls))	# Iteramos cada uno de los atributos (diccionario)
	for nombre, atributo in atributos.items():
		print(nombre, atributo)

	# Revisamos si se ha sobrescrito el metodo __init__
	if '__init__' not in atributos.keys():
		raise TypeError(cls.__name, 'no ha sobrescrito el metodo init.')
	return cls

@decorador_repr
class Persona:
	def __init__(self, nombre, apellido):
		print('Se ejecuta el inicializado')
		self._nombre = nombre
		self._apellido = apellido
		
	@property
	def nombre(self):
		return self._nombre
	@property
	def apellido(self):
		return self._apellido
	
perona1 = Persona('Juan', 'Perez')
``` 

Eso quiere decir que cuando se decora una clase, los metodos se enlistan pero no se ejecutan si no hasta que termina el decorador, sin embargo podemos hacer sentencias en el decorador para saber si cuentan con un metodo especificio, en este caso el metodo `__init__`.

Podemos obtener la `firma` de la clase, entre ella los parametros del metodo `__init__` con el método `inspect.signature()`:

```python
import inspect


def decorador_repr(cls):
	print('Se ejecuta decorador')
	print('Recibimos el objeto de clase:', cls.__name__)

	# Revisamos los atributos de clase con el metodo vars
	# Lo volvemos un diccionario
	atributos = dict(vars(cls))	
	for nombre, atributo in atributos.items():   # Iteramos cada uno de los atributos (diccionario)
		print(nombre, atributo)

	# Revisamos si se ha sobrescrito el metodo __init__
	if '__init__' not in atributos.keys():
		raise TypeError(cls.__name, 'no ha sobrescrito el metodo init.')

	# Inspeccionamos la firma del metodo init
	firma_init = inspect.signature(cls.__init__)

	# Recuperamos los parametros excepto el primero (self)
	parametros_init = list(firma_init.parameters)[1:]
	print(parametros_init)

	# Verificamos si cada paremtro tiene un metodo property asociado
	for parametro in parametros_init:
	# Verificamos si de la lista de __atributos__ de la clase, en get (que esta asociado a property) esta el parametro de los parametros_init 
	# Property es un valor de tipo built-in para preguntar si se esta usando el decorador property
		isproperty = isinstance(atributos.get(parametro), property)   # (usamos get para que no vuelva error si no existe la llave)
		if not isproperty:
			raise TypeError('No existe un property para el parametro', parametro)


	# Crear el metodo repr dinamicamente (Debe de contener self ya que sera un metodo agregado a nuestra clase, de lo contario marca error)
	def metodor_repr(self):
		# Obtenemos el nombre de la clase dinamicamente
		clsname = self.__class__.__name__
		# Obtenemos el nombre de sus propiedades dinamicamente
		generador_arg = (f'{nombre}={getattr(self, nombre)!r}' for nombre in parametros_init)  # !r tambien incluye las comillas de la lista
		# Crear Lista de argumentos
		lista_arg = ','.join(list(generador_arg))
		return f'{clsname}({lista_arg})'


	# Para agregar dinamicamente el atributo:
	setattr(cls, '__repr__', metodor_repr)
	return cls

@decorador_repr
class Persona:
	def __init__(self, nombre, apellido):
		print('Se ejecuta el inicializado')
		self._nombre = nombre
		self._apellido = apellido
		
	@property
	def nombre(self):
		return self._nombre
	@property
	def apellido(self):
		return self._apellido
	
persona1 = Persona('Juan', 'Perez')
print(persona1)

print(dir(Persona))
codigo_repr = inspect.getsource(persona1.__repr__)
print(codigo_repr)
```