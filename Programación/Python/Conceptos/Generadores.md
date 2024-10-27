#Python #Generadores

Un generador es una funcion especial que retorna varios valores pero no de forma directa, si no secuencial y suspende su funcionamiento hasta que se entrega el siguiente valor,  hace uso de la palabra reservada `yield` = `producir`. No se usa `return`.

```python
def generador():
	yield 1
	yield 2
	yield 3
	yield 4
```

En este caso estamos produciendo secuencialmente cada uno de estos valores. Los generadores se van consumiendo a demanda con la funcion `next`:

```python
gen = generador()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
```

Cada vez que mandemos a llamar a `generador()` se creara un nuevo objeto por consumir de este mismo, por lo que lo correcto es asignarlo a una variable para poder usar el mismo, de lo contario siempre obtendremos el primer valor del generador.

Si le demandamos mas datos de los que le es posible al generador, arroja un error del tipo `StopIteration`,

Podemos consumir los valores del generador __con un ciclo for__:

```python
for valor in generador():
	print('Valor del generador:', valor)
```

## Ejemplos de Uso de Generadores

- Generar números del 1 al 5

```python
def generador_numeros():
	for numero in range(1,6):
		yield numero
		print('Se reanuda el ciclo for')

generador = generador_numeros()

print(f'Objeto generador: {type(generador)}\n{generador}')

for numero in generador:
	print('Numero recuperado del generador', numero)
```

Como se puede ver, como `yield` ya no tenia un numero que producir reanuda la funcion, sale del ciclo for y sale de la función.

- Consumir a demanda:

```python
def generador_numeros():
	for numero in range(1,6):
		yield numero
		print('Se reanuda el ciclo for')

generador = generador_numeros()

print('Consumimos a demanda:', next(generador))
print('Consumimos a demanda:', next(generador))
print('Consumimos a demanda:', next(generador))
```

- Consumir generador con [[Ciclos#Bucle `while`|ciclos while]]:

```python
def generador_numeros():
	for numero in range(1,6):
		yield numero
		print('Se reanuda el ciclo for')

generador = generador_numeros()

while True:
	try:
		valor = next(generador)
		print('Valor del generador:', valor)
	except StopIteration as e:
		print('Se termina la iteracion del generador')
		break
```

Usando `StopIteration` es la forma mas comun de manejar un generador.

## Expresiones Generadoras

Es basicamente un generador anonimo, una expresion de una linea, para ello hacemos uso de un parentesis `()`:

```python
multiplicacion = (valor*valor for valor in range(4))

print(multiplicacion, type(multiplicacion))

print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
```

Tambien podriamos meterlo en una `list()` o `tuple()` para extraer directamente todos los valores del generador a un dato de tipo secuencia.

Podemos pasar los valores de un generador a cualquier funcion e interpretara estos como un dato tipo secuencia:

```python
import math
suma = sum(valor*valor for valor in range(4))

print(suma)
```

Podemos hacer uso de listas o iteradores, esto es util cuando tengamos listas de miles o millones de elementos, los generadores son mas eficientes con la memoria:

```python
lista = ['Juan', 'Perez']
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))
```


> [!info] Es como usar `list()`
> Cuando usamos `[]` para hacer uso de generadores es lo mismo que al final de la expresion convertirlo en lista con `list(generador)`.


Crear un string desde un generador, partiendo de una lista:

```python
lista = ['Kari', 'Gomez', 'Raul', 'Alejandro']
contador = 0

# Definimos una funcion para incrementar el contador
def incrementar():
	global contador
	contador += 1
	return contador

generador = (f'{incrementar()}. {nombre}' for nombre in lista)
# Ahora cada que solicitemos un valor al generador, hara un f-string

# Lo volvemos una lista para todos los yields del generador
lista = list(generador)

# Imprimimos
print(lista)

# Convertimos la lista en una cadena
cadena = ', '.join(lista)
print('Cadena generada', cadena)
```

## Compresión de Listas

`List Comprehensions` es similar al uso de generadores, la unica diferencia es que los generadores utilizan tuplas, este en cambio, usa listas.

- Sin `List Comprehensions`:

```python
numeros = range(10)
# Haremos una lista con los valores pares de numeros elevado al cuadrado
lista_pares = []

for numero in numeros:
	if numero % 2 == 0:
		lista_pares.append(numero*numero)

print('Lista pares:', lista_pares)
```

- Con `List Comprehensions`: `[expresion for var in coleccion if condicion]`, el `if` es opcional:

```python
lista_pares = [numero*numero for numero in range(10) if numero % 2 == 0]

# El mismo resultado con una linea de codigo!
print('Lista pares:', lista_pares)
```

Podemos hacer uso de mas de una condicion, en este caso, si el numero es divisible entre 2 y 3:

```python
lista = [numero*numero for numero in range(50) if numero % 2 == 0 if numero % 3 == 0]

print('Lista resultante', lista)
```

Inclusive podemo hacer uso de `if`, `else`:

```python
# Separar pares e impares:
lista_impares = []
lista_pares = []
[lista_pares.append(numero) if numero % 2 == 0 else lista_impares.append(numero) for numero in range(20)]

print(f'Lista pares: {lista_pares}, Lista impares: {lista_impares}')
```

En este caso, la sentencia es todo: `lista_pares.append(numero) if numero % 2 == 0 else lista_impares.append(numero)`.

#### Con Listas de Listas

Podemos convertir una lista de listas en una simple lista con la compresion de listas:

```python
lista_listas = [[1,2,3],[4,5,6],[7,8,9]]

lista = [valor for lista in lista_listas for valor in lista]

print(lista)
```

Aqui estamos haciendo practicamente dos for anidados en una misma sentencia de compresion de listas.

Ahora podemos procesarlo para extraer a otra lista los numeros pares partiendo de la lista de listas:

```python
lista_listas = [[1,2,3],[4,5,6],[7,8,9]]

lista_pares = [valor for lista in lista_listas for valor in lista if valor % 2 ==0]

print(lista_pares)
```

> [!question] Division Modular `%`
> La division modular (`%`) regresa `1` si la division tuvo residuro, `0` en el caso contrario.
