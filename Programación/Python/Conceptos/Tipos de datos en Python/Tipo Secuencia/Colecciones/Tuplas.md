#Python #Tuple

>Una tupla es un tipo de dato muy similar a una lista pero no se puede modificar, ósea, **es inmutable**.

Definir una tupla es muy similar a las [[Listas]] y datos tipo arreglo, la diferencia es que se usan paréntesis para declararse:

```python
frutas = ('Naranja', 'Platano', 'Guayaba')
```


> [!info]- Variable solo con comas.
> Si a una variable le asignamos diversos valores sin delimitarlo con el tipo de dato a los bordes, se creara automaticamente una tupla.
> ```python
> variable = 1, 2, 3, 4, 5
> print(type(variable))
> ```



> [!WARNING]- NO MODIFICABLE
> Si se intenta cambiar el valor de la tupla, nos dara un error:
> ```python
frutas[0] = 'Pera'

## Crear un Solo Dato Pero de Tipo TUPLA

Para crear una sola literal pero de tipo tupla debemos declararla entre parentesis, con una sola coma despues de esta, ya que si usamos `tuple(var)` obtendremos un error:

- Intentando con `tuple()`:

```python
try:
	variable = 12
	variable = tuple(variable)
	print(type(variable))
except TypeError:
	print(f'Error, no se puede volver una tupla un entero')
```

- Intentando con `(12,)`:
```python
variable = (12,)
print(type(variable))
```

Al igual que todos los datos del tipo arreglo, podemos usar funciones y asignaciones que se utilizan normalmente:

- Saber el largo de una tupla: 
```python
print(len(frutas))
```
- Acceder a un elemento:  
```python
print(frutas[0])
```

- Tambien hay navegacion inversa: 
```python
print(frutas[-1])
```
- Acceder a un rango de valores: 
```python
print(frutas[0:2])
```
- Eliminar la tupla por completo: 
```python
del frutas
```

Podemos hacer un recorrido con un for de los elementos en la tupla, igual que con las listas.

```python
for fruta in frutas:
    print(fruta, end = ' ')
```

>[!question]- `end = ' '`
>Cuando hacemos esto con un print, estamos declarando que cuando termine de imprimir no haga un enter, mejor agregue espacio, esto sirve para cuestiones de formato.

Como ya sabemos, las tuplas son inmutables, pero esto no impide convertirla a una lista para poder modificarla e incluso después remplazarla por la misma tulpa.

```python
frutasList = list(frutas)
frutasList[0] = 'Pera'
frutas = tuple(frutasList)
print('\n', frutas)
```

### Swap de Variables Tupla

Podemos cambiar el orden desempaquetado de una variable hecha con tuplas:

```python
a, b = 'Hola', 'Adios'
print(a, b)
a, b = b, a # Swap
print(a, b)
```

>[!summary]- Conversiones
>![[Conversiones]]
[](Conversiones.md)>Una tupla es un tipo de dato muy similar a una lista pero no se puede modificar, ósea, **es inmutable**.

