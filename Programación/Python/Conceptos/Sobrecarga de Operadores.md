#Python #Sobrecarga

La sobrecarga de operadores significa que un mismo operador puede comportarse de diferentes formas.

### Sobrecarga de `+`:

- Con enteros:
```python
a = 2
b = 3
print(a+b)
```
- Con strings:
```python
a = 'Hola '
b = 'Mundo'
print(a + b)
```
- Con listas:
```python
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(a + b)
```
Para poder usar sobrecarga en clases necesitamos sobrescribir los siguientes métodos dunder:

Operadores Binarios

| Operador | Metodo Dunder               |
|:--------:|:--------------------------- |
|    +     | `__add__(self, other)`      |
|    -     | `__sub__(self, other)`      |
|    *     | `__mul__(self, other)`      |
|    /     | `__turediv__(self, other)`  |
|    //    | `__floordiv__(self, other)` |
|    %     | `__mod__(self, other)`      |
|    **    | `__pow__(self, other)`      |
Operadores de comparacion:

| Operador | Metodo Dunder         |
|:--------:| --------------------- |
|    <     | `__it__(self, other)` |
|    >     | `__gt__(self, other)` |
|    <=    | `__le__(self, other)` |
|    >=    | `__ge__(self, other)` |
|    ==    | `__eq__(self, other)` |
|    !=    | `__ne__(self, other)` |
Operadores de asignacion:

| Operador | Metodo Dunder                |
| -------- | ---------------------------- |
| -=       | `__isub__(self, other)`      |
| +=       | `__iadd__(self, other)`      |
| `*=`     | `__idiv__(self, other)`      |
| /=       | `__ifloordiv__(self, other)` |
| //=      | `__imod__(self, other)`      |
| %=       | `__imod__(self, other)`      |
| **=      | `__ipow__(self, other)`      |

Operadores unarios:


| Operador | Metodo Dunder             |
| -------- | ------------------------- |
| -        | `__neg__(self, other)`    |
| +        | `__pos__(self, other)`    |
| ~        | `__invert__(self, other)` |
Por defecto no podemos sumar `miObjeto1 + miObjeto2`, para poder sobrecargarlo necesitamos sobrescribir el método `__add__` de `MiObjeto`.

```python
class Persona:
	def __init__(self, nombre, edad):
		self._nombre = nombre
		self._edad = edad
	
	@property
	def nombre(self):
		return self._nombre
		
	@property
	def edad(self):
		return self._edad
	# Sobrescribir la suma
	def __add__(self, other):
		return f'{self._nombre} {other.nombre}'
	# Sobrescribir la resta
	def __sub__(self, other):
		return self.edad - other.edad

obj1 = Persona('Juan', 35)
obj2 = Persona('Pedro', 22)

print(obj1 + obj2)
print(obj1 - obj2)

```


> [!summary] Cuando sumamos sustituyendo `__add__`
> Es equivalente `obj1.__add__(obj2)` a `obj1 + obj2`, por lo que el primer objeto que declaremos es el que ejecutara el método `__add__` y tomara como parámetro al primero. Por eso usamos `__add__(self, other)`, el cual es el segundo objeto como parametro.

