#Python #MetodosEstaticos

Así como existen las [[Variables de Clase]], también podemos tener métodos de clase. Hay dos métodos de clase: Los métodos estáticos y los métodos de clase como tal.
## Métodos Estáticos

Los métodos estáticos se asocian directamente con la clase, tal cual como una variable de clase. Se dice que un método estático no tiene información directamente relacionada con nuestra clase. Se define con el siguiente decorador:

```python
class MiClase:
	variable_clase = 'Valor de la variable de clase'
	
	def __init__(self, variable_instancia):
		self.variable_instancia = variable_instancia
	
	@staticmethod   # Ahora se asocia con la clase y no con los objetos
	def metodo_estatico():
		print(MiClase.variable_clase)

MiClase.metodo_estatico()
```

Los métodos estáticos deben acceder a las variables de clase de forma indirecta, ósea, acceder a `ClaseActual.variable_clase`. Se usan cuando quieres seccionar el código de forma lógica perteneciente a una clase.

> [!warning] Un metodo estatico no puede acceder a las variables de instancia (`self`) porque funcionan cuando no hemos definido un objeto.

| Contexto Estático                                                                          | Contexto Dinámico                                                                                                                              |
| ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Es la parte de la clase antes de crear un objeto, osea que meramente pertenece a la clase. | Es la parte de la clase cuando ya se ha definido el objeto, la parte dinamica trabaja con `self`. Solo cuando la clase ya se cargo en memoria. |
## Métodos de Clase

Son métodos que pertenecen a la clase (no al objeto) y pueden acceder directamente a las variables de clase (no de instancia).

```python
class MiClase:
	variable_clase = 'Valor de la variable de clase'
	
	def __init__(self, variable_instancia):
		self.variable_instancia = variable_instancia
	
	@classmethod
	def metodo_clase(cls):
		print(cls.variable_clase)

MiClase.metodo_clase()
```

Ahora el contexto de la clase actual es `cls`, en lugar de decirle que acceda a la clase `NombreClase.variable_clase`, entiende que con ello estamos hablando de la clase actual.

## Contexto Estático y Dinámico

Tambien se puede acceder a nuestros métodos estaticos desde un objeto:

```python
miObjeto1 = MiClase('Valor de la variable de instancia')

MiClase.metodo_clase()
miObjeto1.metodo_clase()
```

Eso significa que los contextos dinámicos si heredan de los estáticos, por ende, cada objeto que creemos de `MiClase` tendrá una `variable_clase` y un `metodo_clase()`, incluso si lo definimos, un `metodo_estatico()` de clase.

> [!important] Acceso:
> Los objetos (contexto estático) si pueden acceder al los contextos dinámicos pero no al revés.

## Diferencias con un Método de Instancia

El método de instancia pude acceder a los métodos de instancia y de clase, a los estáticos y los dinámicos.

```python
class MiClase:
	variable_clase = 'Valor de la variable de clase'
	
	def __init__(self, variable_instancia):
		self.variable_instancia = variable_instancia
		
	@staticmethod
	def metodo_estatico():
		print(MiClase.variable_clase)
		
	@classmethod
	def metodo_clase(cls):
		print(cls.variable_clase)
		
	def metodo_instancia(self):
		self.metodo_clase()
		self.metodo_estatico()
		print(self.variable_instancia)

objeto1 = MiClase('Valor de la variable de instancia')

objeto1.metodo_instancia()
```