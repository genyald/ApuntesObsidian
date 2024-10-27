#Python #Decoradores #Fuctions 

Un decorador en Python es una función que modifica o extiende el comportamiento de otra función o método. Los decoradores permiten "envolver" otra función para extender su funcionalidad sin modificar su código fuente. Su uso es similar al uso de [[Funciones#Función Closure|Funciones Closure]].

Un decorador requiere de una [[Funciones#Funciones Anidadas|Funcion anidada]], ya que la función externa se encarga volver una varible local la funcion a decorar y devolver la funcion ya modificada. La funcion que modifica el comportamiento debe ser interna para poder ser devuelta por el programa.

### Desglosando una Función Decorador:

```python
# Recibimos la funcion original como argumento
def mi_decorador(funcion_original):
	def funcion_modificada():   # Como es una funcion anidada,
								# ahora funcion_original es una local
		print('Comportamiento antes de la funcion')
		funcion_original()
		print('Comportamiento despues de la funcion')
		# Opcionalmente podriamos hacer un return
	return funcion_modificada   # Regresamos la funcion modificada
```
## **Definición del Decorador:**

Funcion decorador:
```python
def mi_decorador(func):
    def funcion_modificada():
        print("Antes de la llamada")
        func()
        print("Después de la llamada")
    return funcion_modificada
```

Función a decorar:
```python
@mi_decorador
def saludar():
    print('¡Hola!')

saludar()  # Ahora cuando llamamos saludar estamos llamando mi_decorador
```

La ventaja de esto es que se puede ocupar en cualquier función:

```python
@mi_decorador
def despedir():
	print('Adios!')

despedir()
```
## Funcionamiento

El decorador `mi_decorador` toma la función `saludar` como argumento y devuelve una nueva función `funcion_modificada`. La función `funcion_modificada` añade comportamiento antes y después de la llamada a `saludar`.

## Decoradores con Argumentos

```python
def repetir(n):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorador
```

## **Aplicación:**

```python
@repetir(3)
def saludar():
    print("¡Hola!")

saludar()
```
## Decoradores con Funciones que Aceptan Argumentos

```python
def decorador(func):
    def funcion_modificada(*args, **kwargs):
        print(f'Llamada a {func.__name__} con args: {args} /kwargs: {kwargs}')
        resultado = func(*args, **kwargs)
        return resultado
	
    return funcion_modificada
```

Es importante aclara que la funcion modificada debe recibir parametros si la funcion original lo hace, por ello se hace uso de `*args`.

**Aplicación:**

```python
@decorador
def sumar(a, b):
    return a + b

print(sumar(3, 5))
```
## Decoradores Anidados

```python
@decorador1
@decorador2
def mi_funcion():
    pass
```

**Orden de Aplicación:** Primero se aplica `decorador2`. Luego se aplica `decorador1`.

## Uso Común de Decoradores

**Validación:**

```python
def requiere_autenticacion(func):
    def wrapper(*args, **kwargs):
        if not autenticado():
            raise PermissionError("No autenticado")
        return func(*args, **kwargs)
    return wrapper
```

**Memorización:**

```python
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
```