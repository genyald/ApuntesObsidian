#Python #List #Tuple #Dictionaries #Strings #Set 

La función `zip` (compresor) nos permite juntar uno o mas iterables de cualquier tipo, regresa una tupla iterada dentro de una lista/tupla con cada dato tipo secuencia introducido.

```python
help(zip)
```

Al igual que en otras funciones, una vez consultado el contenido de el objeto que devuelve `zip`, este se destruye, por lo que si se va a procesar se debe almacenar en alguna variable.
## Ejemplo

- Sin `zip`:

```python
numeros = (1, 2, 3, 4)
letras = ['a', 'b', 'c']
mezcla = (letras + numeros)
print(mezcla)
```

- Con `zip`:
```python
numeros = (1, 2, 3, 4)
letras = ['a', 'b', 'c']
mezcla = zip(letras, numeros)
print(tuple(mezcla))
```

Como `zip` devuelve un objeto, debemos iterarlo o convertirlo a una lista/tupla para poder apreciar su contenido.

Si lo pasamos a una variable que lo convierte en una lista, podemos conservarlo:

```python
numeros = (1, 2, 3, 4)
letras = ['a', 'b', 'c']
mezcla = list(zip(letras, numeros))
print(mezcla)
print(mezcla)
```

Si preguntamos el tipo obtendremos que pertenece a `<class: zip>`.

La funcion `zip` esta limitada a funcionar solamente con el elemento iterable mas pequeño o con menos elementos:

```python
numeros = (1, 2, 3, 4)
letras = ['a', 'b', 'c']
identificadores = 321, 213, 432, 4321, 231
conjunto = {9,8,7,6,5,4,3,2}
mezcla = zip(numeros, letras, identificadores, conjunto)
print(list(mezcla))
```

En este caso, como manejamos un [[Set]], el orden en que se acomodara es meramente aleatorio.

## Iteracion en Paralelo con Zip

Gracias a que podemos trabjar con varios iterables al mismo tiempo, significa que podemos trabajar en paralelo con ellos, para ello hacemos 

```python
numeros = (1, 2, 3, 4)
letras = ['a', 'b', 'c']
identificadores = 321, 213, 432, 4321, 231
conjunto = {9,8,7,6,5,4,3,2}

for numero, letra, id, aleatorio in zip(numeros, letras, identificadores, conjunto):
	print(f'Numero: {numero}, Letra: {letra}, id: {id}, Conjunto: {aleatorio}')
```

Las variables se alinean paralelamente a cada una del contenido en `zip`, esto permite que nuestro `for` sea aumentado paralelamente, en lugar de declarar una variable que aumentaremos en cada ciclo para asignarlo al id de cada variable, haciendo mas ligero nuestro código.

Con el uso de esta herramienta podemos iterar en paralelo para almacenar en listas, entre otras muchas alternativas, ahorrando muchisimas lineas de código.

## Unzip

Podemos simular el comportamiento inverso, pasando de un dato iterable a una variable especifica para poder descomprimirla, para tenemos que tener el resultado de haber hecho `zip` o el equivalente:

```python
mezcla = [(1, 'a', 10), (2, 'b', 11), (3, 'c', 12)]
numeros, letras, ides = zip(*mezcla)
print(numeros, letras, ides)
```

Lo que esta pasando aqui, es que al desempaquetar la lista, la estamos dando como tres tuplas diferentes, estas tuplas se interpolan, por lo que tomara el primero de cada una y formara una tupla, el segundo de cada una y hara otra, asi sucesivamente. Estas tuplas las va a devolver en forma de tuplas, si usamos desempaquetamiento por asignación, cada una de las tuplas se asigna a cada variable, por lo que al final hacemos el proceso inverso.

## Ordenar un zip

Cuando mezclamos iterables, podemos agregar un cierto ordenamiento a estos:

```python
letras = ['c', 'd', 'a', 'e', 'b', 'a']
numeros = [3, 2, 4, 1, 0, 0]
mezcla = list(zip(letras, numeros))

print(f'Sin ordenar: {mezcla}')
print(f'Ordenado: {sorted(mezcla)}')
```

Se ordena en prioridad el primer valor de la tupla, si esta duplicado se va a al siguiente.

### Crear diccionario con Zip y Dos Iterables

En este caso, uno de los iterables sera la llave y el otro el contenido del diccionario, para ello usamos `dict(llave, valor)`, `zip` los convierte en tuplas ya ordenadas en `llave, valor` y se le envia a la funcion diccionario, la cual entiende que estan limitadas por tuplas.

```python
llaves = ['Nombre', 'Apellido', 'Edad']
valores = ('Juan', 'Perez', 34)
diccionario = dict(zip(llaves, valores))
print(diccionario)
```

Para actualizar algun elemento de nuestro diccionario usando la funcion `zip`, formando el par a remplazar e introduciendolo a la funcion `.update()`:

```python
llave = ['Edad']
nueva_edad = [28]
diccionario.update(zip(llave, nueva_edad))
print(diccionario)
```

Esto funciona porque `zip` regresa un _objeto_ iterable con `keys`, lo cual es requerido para que funcione el metodo `.update()`.

>- Si agregamos una llave que no existe, se agregará al diccionario y no se modificará.

> [!success] Saber funciones presentes en python
> Podemos consultar todas las funciones presentes en python mediante la siguiente sentencia:
> ```python
> print(dir(__builtins__))
>```

