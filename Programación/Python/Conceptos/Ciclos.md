#Python #Cicles

Son ciclos o bucles que se usan para ejecutar repetidamente un bloque de codigo para iterar en una secuencia de elementos.

## Bucle `for`

El bucle `for` se usa para iterar sobre una secuencia (tales como una lista, una tupla, diccaionario, conjunto o cadena).

### Sintaxis
```python
for variables in secuencia:
	# Bloque de codigo
```

### Ejemplos
- Iterar sobre una lista:
```python
frutas = ['Manzana', 'Platano', 'Cereza']
for fruta in frutas:
	  print(fruta)
	  # Fruta es la variable temporal donde en el ciclo se maneja su valor actual, por ejemplo, para la iteracion dos, su valor sera 'Platano'
```

- Iterar sobre una cadena:
```python
for letra in 'Python':
	print(letra)
```

- Iterar sobre un rango de numeros:
```python
for i in range(5):
	print(i) # Imprimira del 0 al 4
```
- Iterar sobre un diccionario:
```python
diccionario = {'Nombre': 'Juan', 'Edad': 30}
for clave, valor in diccionario.items():
	print(clave, valor)
```

### Range

`range()` es una funcion que nos permite hacer un for muy especifico, como en c, que elegimos que hacemos con la variable que lo controla, cuanto aumenta y demas. 

La función `range()` puede ser utilizada de tres maneras diferentes:

1. `range(stop)`
2. `range(start, stop)`
3. `range(start, stop, step)`

### Descripción de los parámetros

1. **`stop`**: El número hasta el cual se genera la secuencia (excluyendo `stop`).
2. **`start`**: El número desde el cual se inicia la secuencia (incluyendo `start`). El valor por defecto es 0.
3. **`step`**: El valor de incremento entre cada número en la secuencia. El valor por defecto es 1. Puede ser negativo para contar hacia atrás.

## Bucle `while`

El bucle `while` se usa para ejcturar un bloque de codigo repetidamente mientras se cumpla una condición.

### Sintaxis

```python
while condicion:
	# Bloque de codigo
```

### Ejemplos

- Bucle basico `while`
```python
contador = 0
while contador < 5:
	print(contador)
	contador += 1
```

- Bucle `while` con condición:
```python
respuesta = ''
while respuesta != 'salir':
	respuesta = input('Escribe "salir" para terminar: ')
```

## Control de Bucles

Python proporciona instrucciones para controlar la ejecucion de los bucles con `break`, `continue` y `else`.

 #Break #Continue #Else
### > `break`: Salir del bucle inmediatamente

```python
for i in range(10):
	if i == 5:
		break
	print(i)   # No podra llegar al 9, teminara el bucle cuando llegue a la 5ta iteracion
```

### > `contiune`: Omitir el resto de codigo del bucle

```python
for i in range(10):
	if i % 2 == 0:
	 continue
	print(i)
# Imprime los numeros impares del uno al nueve
```

### > `else` en bucles: Cuando el bucle ha terminado

```python 
for i in range(10):
	print(i)
else:
	print('El bucle ha terminado')
```


