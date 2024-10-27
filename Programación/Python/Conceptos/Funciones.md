#Python #Fuctions

Una funcion es un bloque de codigo que se ejecuta cuando esta funcion es mandada a llamar.

```python
def miFuncion():
	print('Saludos desde mi funcion')

miFuncion()   # Se puede mandar a llamar las veces que sea
```

> [!info] No se puede mandar a llamar una funcion si no se ha escrito o importado

### Parametros a una funcion

Se le puede enviar información a una funcion para que nos devuelva un valor de cualquier tipo, a este valor enviado se le conoce como parámetro.

```python
def funcionx(nombre, apellido):
	print(f'Mi nombre es {nombre} {apellido}')

funcionx('Geny', 'Ochoa')
funcionx('Aldair', 'Romero')
```

### Regresar un valor

Podemos regresar un valor de cualquier tipo al momento de finalizar una funcion.

```python
def sumar(a, b):
	return a + b
	
resultado = sumar(5,3)
print(resultado)
```

**Se le puede asignar valores por defecto a nuestros parametros**  por si al momento de ser llamados no se les otorga un valor. Inclusive se puede agregar un hint de el valor que solicitamos en la funcion, asi como el de salida para una futura documentación.

```python
def sumar(a:int = 0, b:int = 0) -> int:   # Sugerencias
	return a + b
	
resultado = sumar()   # Ahora se puede ejecutar sin otrogarle un valor
print(resultado)
```

### Argumentos variables

Podemos definir una función con parámetros a la cual no conocemos la cantidad que le vamos a entregar. 
```python
def listaNombres(*nombres):
	for nombre in nombres:
		print(nombre)

listaNombres('Raul', 'Pedro', 'Juan', 'Casimiro') # SE CONVIERTE EN TUPLA
```

Podemos darle diferentes tipos de datos a nuestros parámetros:

- Con diccionarios;

```python
def listarTerminos(**kwargs): # Kwargs es opcional, puede ser cualquier otro
	for llave, valor in kwargs.items():
		print(f'{llave} : {valor}')

listarTerminos(IDE = 'Integrated Development Enviroment')
listarTerminos(DBMS = 'Database Mangament System')
```

- Con otros tipos de datos:
```python
def desplegarNombre(nombres): # Intentamos tratarla como lista
	for nombre in nombres:
		print(nombre)

nombres = ['Juan', 'Karla', 'Pedro']
desplegarNombre(nombres)
```

Como se puede observar, una función a la que le damos un tipo de dato especifico

### Distintos tipos de datos como argumentos en python

Podemos declarar el tipo de argumento a enviar inclusive empaquetado. (se debe de empaquetar posteriormente)

```python
def printNombres(nombres):
	for nombre in nombres:
		print(nombre)

nombres = ['Juan', 'Karla', 'Pedro']
printNombres(nombres)

printNombres(['Juan', 'Perro malvado', 'Gatito']) # Asignacion directa de lista como argumentos

printNombres('Karla') # Asignacion de caracteres como argumento

# Error: Le estamos enviando argumentos de mas
# printNombres(10, 11)

printNombres((10, 11)) # Asignacion de una tupla de caracteres como argumento
```

> [!INFO] PARA N PARAMETROS
> Cuando se usa el asterisco para usar n parametros, python lo considera una tupla.



# Funciones recursivas

Una función recursiva es aquella que se manda a llamar a si misma. Un claro ejemplo de este tipo de codigos es el de obtener numeros factoriales:

```python
# Si: 5! = 5 * 4 * 3 * * 2 * 1
def factorial(numero: int = 0):
	if numero == 1:
		return 1   # Retornamos uno a todas las llamadas pendientes que teniamos del else
	else:
		return numero * factorial(numero - 1) # retornamos el valor del numero multiplicado por la misma funcion con el 5 reducido en uno

resultado = factorial(5)
print(f'El factorial de 5 es {resultado}')
```


## Regresar Varios Valores

Podemos devolver mas de un valor, de manera de tupla, que posteriormente se puede desempaquetar o usar asignacion de variable al creearla:

```python
def minmax(elementos):
	return min(elementos), max(elementos)

minimo, maximo = minmax([1,2,3,4,5])
print(f'Valor minimo: {minimo}, Valor Maximo: {maximo}')
```

No es una buena practica devolver muchos valores, dos o tres como máximo esta bien.


> [!question] Metodos de Listas
> Muchos de los métodos de [[Listas]] __QUE NO MODIFICAN__ el contenido, pueden ser usados con tuplas, algunos que si lo hacen, deben ser asignados a una variable para el `return`.
> ```python
> valores = (1, 2, 3, 4, 5)
> indice5 = valores.index(5)
> print(f'Ubicacion de el valor "5": {indice5}')
>```

## Funciones Anidadas

Una funcion anidada es una funcion que cuenta con otra. Recordando que debemeos llamarla inclusive dentro de la primera:

```python
def calculadora(a, b, operacion='sumar'):
	# 1. Definir funcion Anidada
	def sumar(a, b):
		return a + b
	
	def restar(a, b):
		return a - b

	# 2. Mandar a llamar a la funcion anidada:
	if operacion == 'sumar':
		print(f'Resultado de la suma: {sumar(a,b)}')
	elif operacion == 'restar':
		print(f'Resultado de la resta: {restar(a,b)}')

calculadora(5, 6, 'restar')
```

Las funciones internas o funciones anidadas solo pueden ser llamadas desde la funcion externa, por lo que no es como el caso de una clase.

## Usos de Funciones

Las funciones en python, son ciudadanas de primera clase (_firt class citizens_), esto significa que una funcion en python la podemos definir en cualquier parte de nuestro codigo, a diferencia de otros lenguajes de programacion que necesita ser forzosamente una variable de clase. Ademas tambien podemos pasar una funcion como argumento, podemos asignar una funcion a una variable, ademas podemos retornar funciones. Podemos trabajar con funciones prácticamente como si fueran objetos.

>1. Para asignarle una funcion a una variable

- Definimos una función a utilizar:

	```python
	def sumar(a, b):
		return a + b
	```

- Para asignar una funcion a una variable lo hacemos sin uso de parentesis, de lo contrario se manda a llamar y lo que queremos es asignar toda la funcion a la variable:

	```python
	# Asignamos la referencia a la funcion en la variable (mi_funcion):
	mi_funcion = sumar
	```

Así que `mi_funcion` ahora es del tipo `function`:

```python
type(mi_funcion)
```

Ahora podemos mandar a llamar la funcion `sumar` a travez de la variable `mi_funcion`:

```python
resultado = mi_funcion(1, 5)
print('Resultado de la suma:', resultado)
```

>2. Para pasar una función como argumentos a otra función:

- Declaramos nuestra función, posteriormente en la segunda función a la variable que se espera sera una funcion le damos los parámetros con su respectivo parentesis. Posteriormente cuando llamemos la funcion prinicipal, el parámetro debe ser la funcion sin paréntesis:

	```python
	def sumar(a, b):
		return a + b
	
	def operacion(a, b, sumar_arg):
		print(f'Restulado de suma: {sumar_arg(a, b)}')
	
	operacion(4, 5, sumar)
	```

>3. Para retornar una función:

```python
def sumar(a, b):
	return a + b

def retornar_funcion():
	print('Retornamos una funcion')
	return sumar

ref_sumar = retornar_funcion()
print(ref_sumar(2, 5))
```

## Funciones Lambda (λ)

Las funciones lambda es una función anónima (sin nombre), además pequeña (una linea de código). A diferencia de las funciones normales, este tipo de funciones pueden ser asignadas directamente a una variable, no necestian parentesis para los parametros ni usa `return` aunque si regresa una expresión valida y debe tener una referencia para poder ser ejecutada.

Para entenderlas correctamente, podemos comparar una función normal con una función lambda:

```python
# Funcion comun
# def sumar(a, b):   # Si tiene un nombre
# 	return a + b

# Funcion lambda
mi_funcion_lambda = lambda a, b: a + b
# La ejecutamos normalmente
print(mi_funcion_lambda(5, 7))
```

También _podemos hacer uso de una funcion lambda que no recibe argumentos_ (si debemos regresar una expresión valida):

```python
funcion_lambda = lambda: 'Funcion sin argumentos'
print(funcion_lambda())
```

Inclusive _podemos asignarle parametros por default_:

```python
funcion_lambda = lambda a=1, b=6: a + b
print(funcion_lambda())
```

Por ultimo, podemos hacer uso de `*args` y `**kwargs`:

```python
funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)
print('Resultado suma args y kwargs', funcion_lambda(1, 2, 3, a=4, b=5))
```

Aqui hacemos uso de todos estos conceptos:

```python
funcion_lambda = lambda a, b, c=3, *args, **kwargs: a + b + c + len(args) + len(kwargs)
print('Resultado de la suma de todo', funcion_lambda(1,2,3, 4,5,6, e=1, f=2))
```

## Función Closure

Una funcion de tipo closure es una funcion que a su vez encapsula otra función y a diferencia de las [[Funciones#Funciones Anidadas|Funciones Anidadas]] estas mantienen un estado. Una función tipo `closure` puede definir otra función y además la puede regresar. La función interna mandada a llamar puede acceder a las variables globales.

En este caso, la variable local externa son `a` y `b`, ya que la función `operacion` se las otorga a `sumar()`:

```python
# Funcion principal
def operacion(a,b):
	# Definimos una funcion interna o anidada
	def sumar():
		return a + b
	# Retornar la funcion
	return sumar

mi_funcion_closure = operacion(5, 7)
print('Resultado de la funcion closure:', mi_funcion_closure())
```

Entonces, mandamos a llamar a la funcion `operacion` con los respectivos valores de `a` y `b`, esto nos regresa una referencia a la funcion `sumar`, la cual, ya cuenta con los atributos anteriormente dados (`a` y `b`), finalmente mandamos a llamar `mi_funcion_closure()` que es una referencia a `sumar` y este ejecuta la operacion con los valores dados anteriormente. Esto es muy util para hacer secuencial un proceso de varios pasos, como las funciones normales de matlab.

Tambien podemos mandar a llamar al vuelo nuestra funcion para no ejecutarla en dos pasos:

```python
print('Resultado de la funcion al vuelo:', operacion(2, 3)())
```

Aqui mandamos a llamar la funcion operacion con los argumentos `2, 3`, lo cual regresa la funcion sumar, la cual estamos mandando a ejecutar al regresarse con `()`.

### Combinar Closure y Lambda

Podemos combinar los conceptos de [[Funciones#Función Closure|Funcion Closure]] y [[Funciones#Funciones Lambda (λ)|Función Lambda]] para simplificar la sintaxis de los ejemplos anteriores:

```python
def operacion(a, b):
	return lambda: a + b

print('Resultado de la funcion al vuelo:', operacion(2, 3)())
```

Pero inclusive, podemos meter una fucion lambda dentro de una funcion lambda:

```python
operacion = lambda a, b: (lambda: a + b)

print('Resultado de la funcion al vuelo:', operacion(2, 3)())
```