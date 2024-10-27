#Python #ContextManager #With

 La correcta sintaxis del codigo para **abrir un archivo** debe ser un `try`, un `except` y un `finally` que haga un `file.close()`, sin embargo, hay una forma simplificada de hacer esto y es el bloque `with`:
```python
with open('prueba.txt', 'r', encoding = 'utf8') as file:
    contenido = file.read()

with open('prueba.txt', 'w') as file:
    file.write('Texto a escribir\n')
```

Las funciones que dunder que manda a llamar son:
- `__enter__` - Es el metodo donde se abre el recurso ^enter
- `__exit__` -  Es donde se va a salir de forma automatica del recurso ^exit

Gracias a esto, ahora de manera automatica abre el archivo y tambien lo cierra. A esto se le conoce como Context Manager o Administrador de Recursos.

![[context Manager.png]]

## Crear Nuestra Propia Clase con el Context Manager

Esta clase no debe extender de otra clase en particular, solo debe implementar los dos metodos [[Manejo de Contexto `with`#^enter|__enter__]] y [[Manejo de Contexto `with`#^exit|__exit__]]. Esta clase tambien sirve para recursos como base de datos.
```python
class ManejoArchivos:
	def __init__(self, nombre):
		self._nombre = nombre
		
	def __enter__(self):
		print('Estamos entrando al Recurso'.center(50, '-'))
		# Regresamos el objeto constuido para que usen 'as xxxxx'
		self._nombre = open(self._nombre, 'r', encoding = 'utf8')
		return self._nombre
		
	def __exit__(self, tipo_excepcion, valor_excepcion, traceback):
		print('Cerramos el recurso'.center(50, '-'))
		# Verificar si self._nombre esta apuntando aun a un objeto, significa que el rescurso esta abierto:
		if self._nombre:
			self._nombre.close()
```

>- Traceback (traza) = Toda la lista de errores, si es que ocurrió alguno.
>- Firma de metodo = Son los parametros que debemos agregar, de lo contrario obtendremos un error.

Ahora hacemos uso de nuestra clase de Administrador de Recursos:

```python
with ManejoArchivos('prueba.txt') as archivo:
	print(archivo.read())
```

> [!success] Objeto existe:
> ![[Variables#Verificar si una variable existe]]
