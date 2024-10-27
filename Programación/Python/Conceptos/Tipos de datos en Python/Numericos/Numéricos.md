#Python #Datos

>Son datos que contienen únicamente números y no caracteres, existen tres tipos:
## Enteros

>Cuentan unicamente con la parte entera, este tipo de datos descartaran los puntos decimales, por lo que puede servir facilmente para eliminar los decimales de un flotante.

```python
x = 10
```

## Flotantes

Son las variables que se manejaran con punto decimal, normalmente solo hay que agregarle puntos decimales al ser declaradas.

```python
x = 10.245
print(x)
print(type(x))
```

Podemos indicar cuantos puntos decimales mostrar a la hora de imprimir:

```python
x = 10.245
print('{:.2f}'.format(x))
print(f'{x:.2f}')
```

Podemos usar el contructor de clase `float()` para convertir un numero al tipo flotante:
```python
a = float(10)
print(f'a = {a:.2f}')
```

Tambien es valido hacerlo con [[Cadenas|str's]], por lo que el metodo `float` esta [[Sobrecarga de Operadores|sobrecargado]].

```python
a = float('10')
print(a)
```

### Notacion Exponencial (`*10^e = e`)

```python
a = 3e3
print(a)

b = 3e-6
print(f'{b:.5f}')
```


> [!important] Cualquier calculo que lleve un `valor flotante`, hace que todo lo que maneja se vuelva del tipo flotante:
> ```python
> c = 4 + 5.5
> print(type(c))
> ```


## Complejos

>Son variables que como dice su nombre, pertenecen al plano complejo (Ya tienes conocimiento de esto). Se puden declarar directamente:

```python
z = 3 + 2j
z_2 = 6 + 23j
# O tambien
z = complex(3,2)
print(type(z))
```

Para acceder a la parte real o a la parte imaginaria:
```python
z_real = z.real
z_imag = z.imag
print(z_real)
print(z_imag)
```

### Operaciones Complejas

Python nos permite trabajar con diversas operaciones con los complejos, lo cual nos facilita mucho la vida para hacer programas que hagan un proceso dado por nosotros:

> Suma

```python
z_t = z + z_2
print(z_t)
```

> Resta

```python
z_t = z - z_2
print(z_t)
```

> Multiplicación

```python
z_t = z * z_2
print(z_t)
```

> División

```python
z_t = z / z_2
print(z_t)
```

### Funciones con números complejos

En el modulo [[cmath]] tenemos varias funciones par operar con numero complejos.

---
## Type

Podemos saber que tipo de variable es la que tenemos en una variable con la siguiente función:

```python
x = 10
print(x)
print(type(x))
```

```python
x = 'Hola mundo'
print(type(x))
```

> [!info] Declaración
Como se puede apreciar, python decide automáticamente que tipo de variable será dependiendo de el tipo de valor asignado, lo cual nos facilitara en diversas ocasiones el trabajo de declarar el tipo de variable, aunque para aplicaciones muy especificas es probable que necesites declarar que tipo de variable es, inclusive su tamaño.

## Valores Infinitos ∞

En python podemos representar valores infinitos positivos o negativos. Para manejarlos hacemos uso del constructor de la clase `float()`:

```python
infinito_positivo = float('inf')
print(infinito_positivo)
```

Para asegurarnos que el numero es verdaderamente infinito, podemos hacer uso de la biblioteca `math`, ya que tiene un modulo para preguntar si una variable/literal es infinita haciendo uso de `math.isinf()`:

```python
import math
print(f'Es infinito: {math.isinf(infinito_positivo)}')
```

Si nos saltasemos el constructor de la clase `float` obtendriamos:

```python
fake_inf = 'inf'
print(f'Es infinito: {math.isinf(fake_inf)}')
```

Para asignar un infinito negativo:

```python
import math
inf_neg = float('-inf')
inf_neg += 1000 
print(f'Infinito negativo: {inf_neg} :{math.isinf(inf_neg)}')
```

> [!question] Mas formas de declarar Infinitos:
>- Haciendo uso de `math`: `math.inf`/`-math.inf`
>- Haciendo uso de `decimal/Decimal`: `Decimal('Infinity')`/`Decimal('-Infinity')


## Tipo Nan (Not a Number)

Son valores numéricos que significan una indeterminación. Para crearlos podemos hacer uso de tres formas:

```python
import math
from decimal import Decimal

a = float('NaN')
print(f'No es un Numero (float): {math.isnan(a)}')

b = Decimal('NaN')
print(f'No es un Numero (Decimal): {math.isnan(b)}')

c = math.nan
print(f'No es un Numero (math): {math.isnan(c)}')
```

Como se pude observar, podemos usar `math`, especificamente la funcion `math.isnan(valor)` para preguntar si un valor es  un tipo `NaN`.

Cuando declaramos el `NaN` no es sensible a mayusculas, pero lo ponemos asi para leer mas fácilmente el codigo.