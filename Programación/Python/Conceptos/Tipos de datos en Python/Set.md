#Python #Set

Un set no mantiene un orden, no se puede modificar manualmente, solamente podemos quitar o agregar elementos, tampoco permite elementos duplicados (no causa efecto), se crea con corchetes:

```python
mi_set = {1, 2.2, 3.0, 4.9, 'Texto', False}
print(type(mi_set))
```

Para consultar información especifica:

```python
help(set)
```

**Los Elementos de un Set son Inmutables**, osea que no pueden almacenar listas, unicamente tuplas, strings, floats (enteros se vuelven floats):

```python
try:
	mi_set = {[1,2,3], [4,5,6], [7,8,9]}
	print(mi_set)
except TypeError as e:
	print(f'Error del tipo {type(e)}: {e}')
```

Para definir un set
```python
planetas = {'Marte', 'Jupiter', 'Venus'}
```


> [!WARNING]- ¿ Un set vacio?
> Si usamos `mi_set = {}`, en realidad estamos creando un [[Diccionarios|diccionario]] vacio:
> ```python
>mi_set = {}
>print(type(mi_set))
>```
>La forma correcta de crear un `set vacio` es la siguiente:
>```run-python
>mi_set = set()
>print(type(mi_set))
>```

Podemos crear un set partiendo de un dato de tipo secuencia:

```python
datos = [1,2,3,4,5]
datos2 = (1,2,3,4,5)
datos3 = {'Uno':1, 'Dos':2, 'Tres':3}
print(type(datos), type(datos2), type(datos3))
datos = set(datos)
datos2 = set(datos2)
datos3 = set(datos3)
print(type(datos), type(datos2), type(datos3))
print(f'Diccionario convertido: {datos3}')
```

>Entonces si volvemos un set un diccionario, solamente estaremos tomando las llaves, a menos que dejemos explicicto lo contrario.

Para medir el tamaño de un set, usamos len():

```python
print(len(planetas))
```

Para revisar si algún elemento elemento esta presente en nuestro set:
```python
print('Marte' in planetas)
```

Para agregar un elemento a nuestro set:
```python
planetas.add('Tierra')
```

Tambien podemos introducir un datos tipo secuencia en uno mismo, unclusive otro set, haciendo uso de `update`:

```python
conjunto = {1,2,3,4,5}
conjunto2 = {6,7,8,9}
print(conjunto)
conjunto.update(conjunto2)
print(conjunto)
```

Para remover un elemento de nuestro set, usamos **.remove**, pero **esto arroja un error si el elemento no existe**.

```python
planetas.remove('Tierra')
```

La forma de evitar esto es usando discard:

```python
planetas.discard('Tierra')
```

Podemos hacer una copia `Shallow` (poco profunda) haciendo uso de `.copy()`:
```python
conjunto = {1,2,3,4,5}
print(conjunto)
conjunto2 = conjunto.copy()
print(conjunto == conjunto2)
```

Para limpiar y para eliminar usamos clear y del, respectivamente:

```python
planetas.clear()
del planetas    # Este destruye totalmente nuestra variable
```

>[!info]  Elementos duplicados
>En un set, no se permiten elementos duplicados, por lo que agregar un elemento que ya existe, no efectuara ningun cambio en nuestro set.

### Operaciones Algebraicas con Set's

#Conjuntos #OperacionConjuntos

Podemos hacer tipoos de operaciones de conjunto nativamente:

![[Operaciones_set.png]]

Para ello vamos a crear varjios set's con diferentes atributos de personas:

```python
pelo_negro = {'Juan', 'Karla', 'Pedro', 'Maria'}
pelo_rubio = {'Lorenzo', 'Laura', 'Marco'}
ojos_cafe = {'Karla', 'Laura'}
menores_30 = {'Juan', 'Karla', 'Maria'}
```

^e7703e


Con esto presente, podemos hacer uso de cada uno de los operadores de conjunto:

- `UNION`: Juntar personas de `pelo_rubio` y `ojos_cafe` (No se repiten nombres):

	```python
	print(pelo_rubio.union(ojos_cafe))
	```

- `INTERSECCION`: Personas que tienen `pelo_negro` pero también `ojos_cafe`:

	```python
	print(pelo_negro.intersection(ojos_cafe))
	```

- `DIFFERENCE` (NO CONMUTATIVA): Resta de dos conjuntos, en este caso, `personas menores_30` y `pelo_negro`:

	```python
	print(pelo_negro.difference(menores_30))
	```

- `SIMETRIC DIFFERENCE`: Conjuntos en comun se dercartan y los une, en este caso personas con `pelo_negro` u `ojos_cafe`:

	```python
	print(pelo_negro.symmetric_difference(ojos_cafe))
	```

> [!NOTE] `Propiedad Conmutativa`
> Como es un `set`, el orden del operando y el operador no afectara el resultado (exceptuando `DIFFERENCE`. A esto se le conoce como propiedad `conmutativa`.

### Preguntas con SET

Podemos hacer preguntas condicionales para saber lo siguiente de dos conjuntos:

![[set_operation.png|600]]

Podemos preguntar si A es un subconjunto de A, si esto es verdadero entonces A es superconjunto de B. También podemos preguntar si A no tiene nada que ver con B.

Podemos continuar haciendo las pruebas con el [[Set#^e7703e|set de personas]] de esta leccion:

- Para saber si B es un subconjunto de A (`menores_30` subconjunto de `pelo_negro)` : 

```python
resp = menores_30.issubset(pelo_negro)
if resp:
	print('menores_30 SI es subset de pelo_negro')
else:
	print('menores_30 NO es un subset de pelo_negro')
```

- Para saber si A es superset de B (En este caso, `pelo_negro` debe ser superset de `menores_30`):

```python
resp = pelo_negro.issuperset(menores_30)
if resp:
	print('pelo_negro SI es superset de menores_30')
else:
	print('pelo_negro NO es un superset de menores_30')
```

- Para saber si A y B no tienen nada que ver (Para saber si las personas de `ojos_cafe` tienen `pelo_rubio`):

```python
resp = ojos_cafe.isdisjoint(pelo_rubio)
if resp:
	print('NO hay nadie con ojos cafe y pelo rubio')
else:
	print('SI hay alguien con ojos cafe y pelo rubio')
```