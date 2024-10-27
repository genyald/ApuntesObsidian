#Python #Booleans

El tipo de dato booleano (`bool`) en Python representa dos valores, `True` o `False`. Sirven para aplicar el algebra de bool y asi controlar el flujo del programa mediante condiciones y bucles.

## Definicion
Puedes definir variables booleanas escribiendo directamente los valores `True` o `False`:
```python
verdadero = True
falso = False
```


## Conversión 

Para convertir algo al tipo booleano usamos la funcion `bool(valor)`. Con las siguientes observaciones:

>Para numericos
- Con un valor numérico que sea `0` obtendremos `False`.
- Con cualquier otro valor numerico que no sea `0` obtendremos `True`.

```python
a = 0
a = bool(a)
print(a)

b = 12
b = bool(b)
print(b)
```

>Para el tipo `str` 
- Obtendremos `False` si es una cadena vacia.
-  Obtendremos `True` si la cadena tiene contenido.
```python
a = ''
a = bool(a)
print(a)

a = 'Hola'
a = bool(b)
print(b)
```

>Para `colecciones`:

- Obtendremos `False` si una lista/tupla esta vacia.
- Obtendremos `True` si una lista/tupla tiene contenido.
```python
a = []
a = bool(a)
print(a)

b = [1, 2, 3]
b = bool(b)
print(b)
```

>Para `diccionarios`:

- Obtendremos `False` si el diccionario esta vacio.
- Obtendremos `True` si el diccionario tiene contenido.

```python
a = {}
a = bool(a)
print(a)

b = {'POO': 'Programacion Orientada a Objetos', 'XD': 'Carita'}
b = bool(b)
print(b)
```


> [!summary] Cuando hacemos `if variable:`
> Entonces, cuando hacemos uso de `if variable:`, realmente estamos haciendo la sentencia: `if bool(variable):`.
> Para Falso:
> ```run-python
> if '':
> 	print('Regreso Verdadero')
> else:
> 	print('Regreso Falso')
> ```
> Para Verdadero:
> ```run-python
> if 'Cadena':
> 	print('Regreso Verdadero')
> else:
> 	print('Regreso Falso')
> ```
> Lo mismo aplica para un ciclo `while`:
> ```python
> contador = 0
>try:
>	while 'Str':
> 		print(f'Ejecucion while: {contador}')
> 		contador += 1
> 		if contador == 10:
> 			break
> finally: 
> 	print('While terminado')
> ```

## Operadores de comparacion

Sirven para comparar dos valores y regresan un valor de tipo booleano nuevamente, entre ellos se encuentran:
- Igual a (`==`)
```python
5 == 5 # True
5 == 3 # False
```

- Diferente o distino de (`!=`):
```python
5 != 3 # True
5 != 5 # False
```

- **Mayor que (`>`)**:

```python
5 > 3  # True 3 > 5  # False
```

- **Menor que (`<`)**:

```python
3 < 5  # True 5 < 3  # False
```

- **Mayor o igual que (`>=`)**:

```python
5 >= 5  # True 3 >= 5  # False
```

- **Menor o igual que (`<=`)**:

```python
3 <= 5  # True 5 <= 3  # False
```

### Operadores Lógicos

Los operadores lógicos se utilizan para combinar valores booleanos:

- **`and`**: Devuelve `True` si ambos operandos son `True`.

```python
True and True  # True True and False  # False
````

- **`or`**: Devuelve `True` si al menos uno de los operandos es `True`.

```python
True or False  # True False or False  # False
````

- **`not`**: Devuelve el valor opuesto.

```python
not True  # False not False  # True
````

## Conversion a Booleano

Cualquier valor en python puede ser evaluado en un contexto booleano, usando la funcion `bool()`. Los valores considerado como `False` seran aquellos que con contengan nada, puede ser una tupla, un diccionario, una cadena, un set, un cero flotante o entero, una lista o cualquier tipo de valor que no cuente con un valor. Por otro lado cualquier dato que cuente con un contenido sera considerado como `True`.

```python
bool(None)  # False
bool(0)  # False
bool('')  # False
bool(123)  # True
bool('Hola')  # True
bool([1, 2, 3])  # True
```