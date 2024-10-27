#Python #Desempaquetamiento

El desempaquetamiento en python permite dividir a los elementos que conforman un tipo de dato secuencial en argumentos individuales. Se usa con operadores como `*` y `**`.

Cuando creamos una variable con varios valores, realmente del lado derecho se esta creando una tupla de valores que se asigna a estos valores:

```python
valores = 1,2,3
print(type(valores))
```

El contexto de desemplaquetamiento o `unpacking` consiste en que del lado derecho podemos asignar lista/tupla pero del lado derecho podemos asignar valores en variables de manera independiente, a esto se le conoce como [[Desempaquetamiento#Desempaquetamiento en Asignaciones|Desempaquetamiento en asignaciones]].

```python
valor1, valor2, valor3 = 1, 2, 3
print(valor1, valor2, valor3)
```

>Podemos omitir un valor de la asignacion usando `_,` (practica común en python):

```python
valor1, _, valor3 = 1, 2, 3
```
## Desempaquetamiento de Tuplas y Listas

### Para mandar a llamar funciones

Cuando usamos `*` al llamar a una funcion, los elementos que conforman esa tupla o lista se envian como argumentos posicionales idividuales.

Con `*`:

```python
def funcion(a, b, c):
	print(a,b,c)

# Tupla
tupla = (1, 2, 3)
funcion(*tupla)

# Lista
lista = [4, 5, 6]
funcion(*lista)
```

Sin `*`:

```python
def funcion(a = 1, b = 2, c = 3):
	print(a, b, c)

# Tupla
tupla = (1 ,2 ,3)
funcion(tupla)

# Se envia como un solo dato, por lo que a seria igual a la tupla

# Lista
lista = [4, 5, 6]
funcion(lista)
```

## Desempaquetamiento Parcial

Podemos desempaquetar solamente algunos de los elementos que requerimos, usando `*` para los elementos restantes:
```python
a, b, *resto = (1, 2, 3, 4, 5)
print(a, b, resto)

x, *medio, y = [7, 8, 9, 10, 11]
print(x, medio, y)
```

Debe haber por lo menos dos variables de asignación.

## Desempaquetamiento de Diccionarios

Usando `**` al llamar a una función, los pares clave-valor del diccionario se pasaron como argumentos de palabras clave:

```python
# Con **
def funcion(nombre = None, edad = None):
	print(nombre, edad)

diccionario = {'nombre' : 'Juan', 'edad' : 25}
funcion(**diccionario)

# Sin **
funcion(diccionario)
```

## Combinacion de diccionarios

Podemos combinar varios diccionarios usando `**`:

```python
# Con **
dic1 = {'a': 1, 'b': 2}
dic2 = {'c': 3, 'd': 4}

combinado = {**dic1, **dic2}
print(combinado)

# Sin **: ERROR
# combinado = {dic1, dic2}
# print(combinado)
```

## Desempaquetamiento al definir una función

`*args` permite pasar un numero variable de argumentos posicionales a una función. Los argumentos se recopilan en un tupla:

```python
def funcion(*args):
	for arg in args:
		print(arg)

funcion(1, 2, 3)
```

### Usando  keyword arguments `*kwargs`:
`**kwargs` permite pasar un numero variable de argumentos de palabras clave a una función. Los argumentos se recompilan en un diccionario:

```python
def funcion(**kwargs):
	for key, value in kwargs.items():
		print(f'{key} : {value}')

funcion(nombre = 'Juan', edad = 25)
```

## Mezcla de argumentos y desempaquetamiento

```python
def mezcla(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key} = {value}")

mezcla(1, 2, 3, 4, 5, nombre='Juan', edad=25)
# Imprime 1, 2, 3, 4, 5, nombre = Juan, edad = 25
```

## Ejemplo de Desempaquetamiento

Para este ejemplo haremos uso de `partition()`, la cual nos divide una cadena en tres partes haciendo uso de un separador. Nos devuelve una tupla, la cual vamos a desempaquetar:

```python
hora = '17:38'
hora, _, minutos = hora.partition(':') # Devolvera 3 valores (Hora, :, Minuto)
print(hora, ':', minutos)
```

## Usos del Desempaquetamiento

#sep

Podemos usar `sep='valor'` para que se imprima este carácter entre cada elemento del print.

```python
numeros = [1, 2, 3]
print(numeros)
print(*numeros, sep='-')
```

Una de las ventajas es que podemos aplicar esto a cualquier iterable.

### En Funciones

Con `*`:

```python
def sumar(a, b, c):
	print(f'Resultado de la suma: {a + b + c}')

numeros = 1, 2, 3
sumar(*numeros)
```

Sin `*`:

```python
def sumar(a, b, c):
	print(f'Resultado de la suma: {a + b + c}')

numeros = 1, 2, 3
sumar(numeros)
```

### Para Unir Listas - Diccionarios - Cadenas

Podemos usar el `*` para crear nuevas listas partiendo de otras, en lugar de crear una lista de listas, ahora desempaquetando podremos formar una nueva lista mas grande:

- Sin `*`:

	```python
	lista = [1, 2, 3]
	lista2 = [4, 5, 6]
	lista3 = [7, 8, 9]
	lista_s = [lista, lista2, lista3]
	
	print(lista_s)
	```

- Con `*`:
	```python
	lista = [1, 2, 3]
	lista2 = [4, 5, 6]
	lista3 = [7, 8, 9]
	lista_s = [*lista, *lista2, *lista3]
	
	print(lista_s)
	```

#### Diccionarios

Para ello necesitamos usar `**kwargs`:

```python
dic1 = {'A':1, 'B':2, 'C':3}
dic2 = {'C': 4, 'D': 5, 'E': 6}

dicc_comp = {**dic1, **dic2}
print(dicc_comp)
```

Practicamente desempaquetamos el texto en bruto dentro de las llaves.

#### Cadenas

Podemos desempaquetar una cadena para formar, por ejemplo una lista con cada uno de los caracteres:

```python
cadena = 'Hola a Todos'
lista = [*cadena]

print(lista)

# Desempaquetamos cada caracter para imprimirlo separado
print(*lista, sep='')
```

Entonces, practicamente tenemos la cadena de texto, la cual desempaquetamos y convertimos en lista, posteriormente al imprimir, volvemos a desempaquetar la lista.