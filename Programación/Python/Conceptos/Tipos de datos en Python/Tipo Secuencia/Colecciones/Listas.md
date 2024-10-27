#Python #List

Para crear una lista en Python, se pueden usar corchetes `[]`, son elementos de coleccion de tipo secuencia que pueden ser mutadas.

Para definir una lista:

```python
# Lista vacía
mi_lista = []

# Lista con elementos
mi_lista = [1, 2, 3, 4, 5]
print(*mi_lista)
```
## Acceder a Elementos

Se puede acceder a los elementos de una lista usando índices, empezando desde 0:
```python
mi_lista = [1, 2, 3, 4, 5]

# Primer elemento
print(mi_lista[0])  # Salida: 1

# Último elemento
print(mi_lista[-1])  # Salida: 5
```
## Slicing (Segmentación)

Es posible obtener una sublista usando slicing:
```python
mi_lista = [1, 2, 3, 4, 5]

# Sublista desde el segundo al cuarto elemento
print(mi_lista[1:4])  # Salida: [2, 3, 4]

# Sublista desde el comienzo hasta el tercer elemento
print(mi_lista[:3])  # Salida: [1, 2, 3]

# Sublista desde el tercer elemento hasta el final
print(mi_lista[2:])  # Salida: [3, 4, 5]
```


> [!Warning] Slicing e índices
> Cuando usamos `slicing`, el primer elemento es `1` y en indices el primer elemento es el `0`.

## Modificar Elementos

Los elementos de una lista pueden ser modificados asignando un nuevo valor al índice:
```python
mi_lista = [1, 2, 3, 4, 5]

# Cambiar el segundo elemento
mi_lista[1] = 20
print(mi_lista)  # Salida: [1, 20, 3, 4, 5]
```

## Invertir una Lista

Para invertir los elementos de una lista, usamos el metodo `.reverse()`, este no devuelve nada, se lo aplica a la lista:

```python
numeros = [1,2,3,4,5]
numeros.reverse()
print(numeros)
```

Podemos usar `reversed()` si queremos el resultado en otra variable:

```python
lista = ['Geny', 'Aldair', 'Ochoa', 'Romero']
lista_ord = reversed(lista)
print((lista_ord))
```

Sin embargo, la salida nos da la direccion de un objeto a itera, por lo iteraramos o convertimos a una lista simple para poder usar su print por defecto:

```python
lista = ['Geny', 'Aldair', 'Ochoa', 'Romero']
lista_ord = reversed(lista)
# Para poder imprimir el contenido

lista_p = list(lista_ord)
print(lista_p)
```


> [!warning] Despues de leer un `reversed()` el contenido se destruye.

## Añadir Elementos

Existen varias formas de añadir elementos a una lista:
```python
mi_lista = [1, 2, 3]

# Añadir un elemento al final
mi_lista.append(4)
print(mi_lista)  # Salida: [1, 2, 3, 4]

# Añadir varios elementos al final
mi_lista.extend([5, 6])
print(mi_lista)  # Salida: [1, 2, 3, 4, 5, 6]

# Insertar un elemento en una posición específica
mi_lista.insert(1, 10)
print(mi_lista)  # Salida: [1, 10, 2, 3, 4, 5, 6]
```

Tambien se pueden juntar listas con el operador `+`, este cuenta con una sobrecarga.
## Eliminar Elementos

Se pueden eliminar elementos de una lista de varias maneras:
```python
mi_lista = [1, 2, 3, 4, 5]

# Eliminar un elemento por su valor
mi_lista.remove(3)
print(mi_lista)  # Salida: [1, 2, 4, 5]

# Eliminar un elemento por su índice y obtener su valor
elemento = mi_lista.pop(2)
print(elemento)  # Salida: 4
print(mi_lista)  # Salida: [1, 2, 5]

# Eliminar el último elemento y obtener su valor
elemento = mi_lista.pop()
print(elemento)  # Salida: 5
print(mi_lista)  # Salida: [1, 2]

# Eliminar todos los elementos de la lista
mi_lista.clear()
print(mi_lista)  # Salida: []
```

## Iterar Sobre una Lista

Se pueden iterar sobre los elementos de una lista usando un bucle `for`:
```python
mi_lista = [1, 2, 3, 4, 5]

for elemento in mi_lista:
    print(elemento)
```

![[Generadores#Compresión de Listas]]
## Operaciones con Listas

Algunas operaciones comunes con listas incluyen:

- Para _obtener el tamaño de una lista_ hacemos uso de `len()`:

	```python
	mi_lista = [1, 2, 3, 4, 5]
	print(len(mi_lista)) 
	```

- Para _verificar si un elemento está en la lista_ usamos `in`:
	```python
	mi_lista = [1, 2, 3, 4, 5]
	print(3 in mi_lista)
	```

- Para _sumar todos los elementos de una lista_ usamos `sum([])`:
	```python
	mi_lista = [1, 2, 3, 4, 5]
	print(sum(mi_lista))
	```
- Para _obtener el minimo de una lista_ usamos `min([])` y para el maximo `max([])`:
	```python
	mi_lista = [1, 2, 3, 4, 5]
	print(min(mi_lista))
	print(max(mi_lista))
	```

- Para _copiar los elementos de una lista_ podemos usar  varios metodos, los principales son:

	1. El metodo `.copy()`, considerando que hace una copia poco profunda, es decir, no duplica los objetos, solo los apuntadores o referencias de memoria a estos. (`Shallow = Poco profunda`):

		```python
		numeros1 = [1, 2, 3, 4, 5]
		numeros2 = numeros1.copy()
		print(numeros2)
		# Preguntamos si la variable apunta a la misma referencia
		print(numeros1 is numeros2)
		# Preguntamos si tienen el mismo contenido
		print(numeros1 == numeros2)
		```
	1. Usando `list()` podemos decirle que forme una lista con otra lista pero asignarlo a otra variable para crear una copia, igualmente es una copia `Shallow`:
		```python
		numeros1 = [1, 2, 3, 4, 5]
		numeros2 = list(numeros1)
		print(numeros2)
		```
	1. Tambien podemos hacer uso de slicing con `:` por si solo, al hacer esto no le estamos asignando un inicio o un final, por lo que se considera toda la lista:
		```python
		numeros = [1,2,3,4,5,6,7,8]
		numeros2 = numeros[:]
		print(numeros2)
		```

>Como esta copia es poco profundo, cuando lo hacemos por ejemplo, con una lista de listas, partiendo de una multiplicacion:


```python
lista_mult = 5*[[2, 5]]
print(lista_mult)
```

En este caso, el objeto `[2,5]` es el mismo, por lo tanto dentro de la lista este objeto esta mandado a llamar varias veces, osea los 5 objetos tienen la misma referencia en memoria.

```python
lista_mult = 5*[[2, 5]]
print(lista_mult[0] is lista_mult[1])
print(lista_mult[0] == lista_mult[1])
```


> [!WARNING] Copiado de Listas
> Todo esto anterior **si** tiene repercusiones en el codigo, ya que si modificamos el elemento en memoria que estamos repitiendo, practicamente estaremos modificando toda la lista:
>```python
lista_mult = 5*[[2, 5]]
print(lista_mult)
lista_mult[0].append(10)
print(lista_mult)
>```



## Ordenar Listas

Se puede ordenar una lista usando los métodos `sort()` y `sorted()`:
```python
mi_lista = [3, 1, 4, 10, 5, 9]

# Ordenar la lista en su lugar
mi_lista.sort()  # Esta es una accion, por lo que no devuelve nada
print(mi_lista)  # Salida: [1, 1, 3, 4, 5, 9]

# Crear una nueva lista ordenada invertida
nueva_lista = sorted(mi_lista, reverse=True)
print(nueva_lista)  # Salida: [9, 5, 4, 3, 1, 1]
```

## Mostrar Índices de Algún Elemento

Para obtener el indice de un elemento que busquemos en una lista, podemos usar el metodo de la clase `list`, especificamente `.index`:

```python
numeros = [1,2,3,4,5]
print('Indice 3:', numeros.index(3))
```

Aqui nos devuelve el indice 2, el cual contiene el valor entero `3`.
## Listas Anidadas

Las listas pueden contener otras listas:

```python
mi_lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Acceder a elementos en listas anidadas
print(mi_lista_anidada[0][1])  # Salida: 2
print(mi_lista_anidada[2][2])  # Salida: 9
```

## Matrices

Como es de suponer, una lista de listas es practicamente una matriz, ya que podemos acceder a esta mediante filas y columnas:

```python
matriz = [[10, 20, 30], [30, 40, 50], [60, 70, 80]]
print(matriz)
# Acceder a un elemento especifico
print('Primer elemento:', matriz[0][0])
```

Para imprimirlo como una matriz podemos hacer uso de un `for`:

```python
matriz = [[10, 20, 30], [30, 40, 50], [60, 70, 80]]
for fila in matriz:
	print(fila)
```

Igualmente, para modificarlo debemos especificar el renglon y la columna:

```python
matriz = [[10, 20, 30], [30, 40, 50], [60, 70, 80]]
for fila in matriz:
	print(fila)
print('Matriz modificada'.center(25, '-'))
matriz[0][2] = 100
for fila in matriz:
	print(fila)
```

### Ordenar una Matriz

Para ordenar una matriz podemos hacer uso del metodo `sort()`:

```python
matriz = [[20, 50, 10], [80, 70, 20], [40, 10, 5]]
# Imprimimos de manera ordenada
for fila in matriz:
	print(fila)
print('Matriz ordenada'.center(25, '-'))
# Ordenamos e imprimimos
for fila in matriz:
	fila.sort()
	print(fila)
```

Tambien podemos ordenar una lista de listas por tamaños con `sort(key=len)`:

```python
matriz = [[20, 50, 10, 30, 100], [80, 70, 60, 20], [40, 10, 5]]
matriz.sort(key=len)
for fila in matriz:
	print(fila)
```

Todos estos metodos funcionan tambien ==para listas de cadenas, se ordenan de forma alfabetica ascendente==, para ello usaremos `sorted()` que tambien es Built-In (Dentro del vanilla) de python:

```python
nombres1 = ['Juan Carlos', 'Karla', 'Pedro', 'Esperanza']
nombres2 = sorted(nombres1)
print(nombres2)
```

Hace practicamente lo mismo que `sort()` pero si devuelve la lista a la salida, por lo que la podemos asignar a una nueva variable. Si quisieramos que se ordene de manera descendente, agregamos la segunda sentencia: `reverese = True`.

- Ordenar por cantidad de caracteres:

	Podemos hacer lo mismo que arriba, en el que ordenamos por el parametro del largo de caracteres: ^OrdenarPorCaracteres

	```python
	nombres1 = ['Juan Carlos', 'Karla', 'Pedro', 'Esperanza']
	nombres_ord = sorted(nombres1, key=len)
	print(nombres_ord)
	```