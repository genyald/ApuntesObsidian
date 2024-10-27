#Python #Clases #Decoradores 

Asi como los decoradores de funciones, tambien contamos con decoradores de clase, algunos ya estan declarados por defecto, asi como el `@classmethod`. Para declarar nuestro propio decorador, debemos crear una funcion que recibe como argumento `cls`. Posteriormente colocamos el nombre de la funcion decoradora con un arroba. 

La funcion decoradora debe regresar `cls` para que se ejecute el metodo decorado de la clase. 

Sin embargo, esto no esta limitado solamente a decorar un metodo. Podemos hacer una función secundaria en la decoradora, esta funcion puede ser susituida por alguna otra con el metodo `setattr(objeto_a_modificar, 'funcion_a_sustituir', funcion_que_susituira)`, con ello podemos remplazar una funcion dunder de cualquier clase.

```python
def decorador(cls):
	print('Funcion decoradora')
	return cls

@decorador
class ClaseDecorada:
	def __init__(self):
		print('Clase inicializada')
		self.imprimir()
		
	def imprimir(self):
		print('Funcion imprimir ejecutada')

objeto = ClaseDecorada()
```

> La funcion decoradora debe de estar declarada antes que la clase.

El orden de ejecucion es:

- Se inicia la clase con sus parametros pero no se inicializa.
- Se ejecuta la funcion decoradora.
- Se inicializa la clase y se crea el objeto.

## Conocer los Atributos de Clase

Podemos usar una función decoradora para procesar previamente los atributos de clase que se le asignaron para inicializar una instancia, esto puede tener el beneficio de hacer que con el decorador cambiemos dimicamente el funcionamiento de alguna funcion conforme a estas variables.

Para conocer estos atributos y metodos hacemos uso de `vars(cls)`, esto nos devuelve un objeto iterable de tipo diccionario, por lo que es recomendable convertirlo en un diccionario: `dict(vars(cls))`. Con esto podemos preguntar si un atributo  o metodo especifico esta inicializado:

```python
def decorador(cls):
	print('Funcion decoradora')
	print(dict(vars(cls)))
	return cls

@decorador
class ClaseDecorada:
	CONST = 'Constante de Clase'
	def __init__(self, texto):
		print('Clase inicializada')
		self.imprimir()
		
	def imprimir(self):
		print('Funcion imprimir ejecutada')

objeto = ClaseDecorada('text')
```

La ventaja de esto es que cuando una función no ha sido sobrescrita no aparece en este diccionario. Por lo que podemos preguntar, por ejemplo, si el metodo `__init__` esta presente. Para ello, como en los [[Diccionarios]] solo preguntamos: `if '__init__' not in atributos.keys()` lo cual nos devuleve un `True` o `False`.

## Recuperar Firma de Algun Metodo

Dentro de la firma de el metodo de una instancia, inclusive antes de ser inicializado, contamos con los parametros dados al objeto, accediendo a ellos podemos hacer aun mas avanzado nuestro decorador, para ello utilizamos la libreria `inspect`.

Posteriormente hacemos uso de `inspect.signature(cls.__init__)` para consultar la firma de el metodo init, el cual es el que cuenta con las variables que se entregan para lanzar una instancia del objeto, esto se devuelve como tupla :

```python
import inspect
def decorador(cls):
	print('Funcion decoradora')
	firma_init = inspect.signature(cls.__init__)
	print(firma_init)
	return cls

@decorador
class ClaseDecorada:
	def __init__(self, texto):
		print('Clase inicializada:', texto)
		self.imprimir()
		
	def imprimir(self):
		print('Funcion imprimir ejecutada')

objeto = ClaseDecorada('Texto entregado a clase')
```

Si queremos asignarla a una variable, debemos agregarle `.parameters` para referirnos a estos especificamente, ya que es un objeto.

Una recomendación para poder comunicar un atributo de clase con su decorador es que este encapsulada, esto es una convencion porque sea como sea es una funcion externa que interactua con la clase.

Podemos preguntar si un atributo de la clase esta encapsulado con `isinstance(atributo, property)`:

#AtributoEncapsulado #isinstance

```python
def decorador(cls):
	print('Funcion decoradora')
	firma_init = list(inspect.signature(cls.__init__).parameters)[1:]
	vars_cls = dict(vars(cls))
	for atributo in firma_init:
		if not isinstance(vars_cls.get(atributo), property):
			raise TypeError('No esta encapsulado el parametro:', atributo)
	return cls

@decorador
class ClaseDecorada:
	def __init__(self, texto):
		print('Clase inicializada:', texto)
		self.imprimir()
		
	def imprimir(self):
		print('Funcion imprimir ejecutada')


objeto = ClaseDecorada('Texto entregado a clase')
```

En la sentencia donde recuperamos la firma, omitimos el primero con `slicing` porque no nos importa `self` para este caso. También para el diccionario de las variables de clase usamos el metodo `.get(atributo_iterado)` para que no devuelva error si no existe.

## Método Dinámico con Decorador de Clase

Podemos crear métodos que modifiquen a la clase conforme sus características, esto es util, por ejemplo para modificar en cada clase el método `__repr__`:

#setattr #RemplazarMetodoCLS

```python
import inspect

def decorador(cls):
    print('Funcion decoradora')
    firma_init = list(inspect.signature(cls.__init__).parameters)[1:]
    print(firma_init)

    def repr(self):
        clsname = self.__class__.__name__
        generador_arg = (f'{nombre}={getattr(self, nombre)!r}' for nombre in firma_init)
        lista_arg = ','.join(list(generador_arg))
        return f'{clsname}({lista_arg})'

    # Remplazamos el metodo __repr__:
    setattr(cls, '__repr__', repr)
    return cls

@decorador
class ClaseDecorada:
    def __init__(self, texto):
        self._texto = texto
        print('Clase inicializada:', texto)
        self.imprimir()

    @property
    def texto(self):
        return self._texto

    def imprimir(self):
        print('Funcion imprimir ejecutada')


objeto = ClaseDecorada('Texto entregado a clase')
print(objeto)
```

Como ahora `repr()` será un método que remplazara a `__repr__` debe contener lo que normalmente este cuenta, para que pueda continuar funcionando, por eso debe tener un parámetro `self`. También hicimos uso de `getattr(objeto, nombre)` para obtener el valor del respectivo valor del atributo del objeto (DEBE CONTENER UN GET).