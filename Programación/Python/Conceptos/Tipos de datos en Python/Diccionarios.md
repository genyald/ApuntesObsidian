#Python #Dictionaries

Los diccionarios son un tipo de dato mutalbe que contiene uno o varios `Índices` (llaves), el cual apunta a un `contenido` de cualquier tipo almacenado en la memoria ROM del programa. El indice o `llave` es inmutable, por lo que solo pueden ser datos de este tipo. 

```python
help(dict)
```

Se declaran de la siguiente manera:

```python
diccionario = {
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
    }
```

Los índices serian 'IDE', 'OOP' y 'DBMS', respectivamente.

- Para imprimir basta con mandar a llamar diccionario dentro de un print.

```python
print(diccionario)
```

### Formas de Recuperar Contenido con su Llave

- La mas común:

```python
diccionario = {'Nombre': 'Juan', 'Apellido': 'Hernandez', 'Edad': 28}
print(diccionario['Apellido'])
```

_Si no encuentra la llave, nos lanza una excepcion del tipo `KeyError`._

- Para evitar un error al ingresar una llave que no existe, usamos el metodo `.get`, ademas podemos regresar un valor en caso que no exista la `llave`: ^getdicc

```python
print(diccionario.get('Oficina', 'No se encontro la llave'))
```

- Si quisieramos que en caso de que la llave no exista y queramos que se agregue para asignarle su respectivo valor, usamos `.setdefault()`:

```python
print(diccionario)
nombre = diccionario.setdefault('Oficina', 'Valor por defecto')
print(diccionario)
```

- Una forma muy facil de imprimir el diccionario es hacer uso del modulo `pprint` (pretty print):

```python
from pprint import pprint as pp

diccionario = {'Nombre': 'Juan', 'Apellido': 'Hernandez', 'Edad': 28, 'Departamento': 'Sistemas'}
pp(diccionario)
```

Por defecto ordena las llaves, si no queremos eso debemos usar: `pp(xxxx, sort_dicts=False)`.

Podemos preguntar el largo con `len()`, podemos acceder a un elemento al igual que con las listas pero con cadenas de texto que refieran al índice, de esta manera accedemos al contenido que pongamos como índice.

```python
# Recuperar el largo
print(len(diccionario))
# Acceder a un elemento con la llave o indice
print(diccionario['IDE'])
# otra forma de recuperar un elemento
print(diccionario.get('OOP'))
```

Para modificar los elementos, se hace igualmente que al imprimir, solo que le declaramos una asignación de valor, en este caso, una cadena de texto ahora en minúsculas.

```python
# modificar elementos de un diccionario
diccionario['IDE'] = 'integrated develoment enviroment'
print(diccionario)
```

> [!question] Llave no existente
> Si agregamos una llave y valor que no existe a un diccionario, esta se agregara automaticamente, si existe se remplaza el valor:
> ```python
>diccionario = {'Nombre': ['Juan', 'Pedro'], 'Apellido': 'Hernandez', 'Edad': 28}
>print(diccionario)
>diccionario['Departamento'] = 'Sistemas'
>print(diccionario)
>```
>Eso significa que no hay valores de llaves duplicados en un diccionario

Para imprimir cada uno de los valores en un recorrido, tenemos que usar .item() y manejarlo como si fuera una tabla, uno será x y el otro y, por lo que tenemos que declarar dos valores dentro del for (termino, valor) que serán los elementos actuales de nuestro barrido.

```python
for  termino, valor in diccionario.items():
    print(termino, valor)
```

Podemos hacer lo mismo, solamente recuperando los términos o llaves, manejándolo con solo un valor en nuestro for.

```python
for termino in diccionario.keys():
    print(termino)
```

Pasa exactamente lo mismo con los valores, solo que hay que usar .values():

```python
for termino in diccionario.values():
    print(termino)
```

Para comprobar la existencia de algun elemento en nuestro diccionario, podemos usar in, lo cual nos devuelve un valor booleano

```python
print('IDE' in diccionario)
```

Finalmente, para agregar elementos o removerlos, asi como limpiar o eliminar nuestro diccionario, tenemos las siguientes sentencias:

```python
# Agregar un elemento a nuestro diccionario 
diccionario['PK'] = 'Primary Key'

# Remover un elemento del diccionario
diccionario.pop('DBMS')

# Limpiar
diccionario.clear()

# Eliminar el diccionario
del diccionario

```

![[Función  Zip#Crear diccionario con Zip y Dos Iterables]]



> [!info] Orden de Diccionarios
> A partir de la version de python `3.7` si guardan un orden, anterior a esto, no lo hacian.
> ```python
>diccionario = {'Nombre': 'Juan', 'Apellido': 'Hernandez', 'Edad': 28}
>print(diccionario)
>```
