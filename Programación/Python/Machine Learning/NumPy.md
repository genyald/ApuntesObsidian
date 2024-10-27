#NumPy #Python 

[Numpy](https://numpy.org) es una librería fundamental para la computación científica con Python.

- Proporciona arrays N-dimensionales.
- Implementa funciones matemáticas sofisticadas.
- Proporciona herramientas para integrar C/C++ y Fortran.
- Proporciona mecanismos para facilitar la realización de tareas relacionadas con álgebra lineal o números aleatorios.

## Instalación

Para instalar NumPy, puedes usar pip:

```bash
pip install numpy
```

## Importación

Para utilizar NumPy en tu proyecto, primero debes importarlo:

```python
import numpy as np
```

---

## Arrays

### Creación de Arrays

Un **array** es una estructura de datos que consiste en una colección de elementos (valores o variables), cada uno identificado por al menos un índice o clave.

![[ArraysNumPy.png]]

* Cada dimensión se denomina **axis**

* El número de dimensiones se denomina **rank**

* La lista de dimensiones con su correspondiente longitud se denomina **shape**

* El número total de elementos (multiplicación de la longitud de las dimensiones) se denomina **size**

```python
# Array cuyos valores son todos 0
a = np.zeros((2, 4))
```

- `np.zeros((2, 4))` - Crea un array de 2x4 lleno de ceros.

> `a` es un array con dos **axis**, el primero de longitud 2 y el segundo de longitud 4, con un **rank** igual a 2, un **shape** igual a (2, 4) y un **size** igual a 8.

### Propiedades de los Arrays

```python
a.shape
```

- `a.shape` - Devuelve la forma del array.

```python
a.ndim
```

- `a.ndim` - Devuelve el número de dimensiones del array.

```python
a.size
```

- `a.size` - Devuelve el número total de elementos en el array.

### Creación de Arrays con Diferentes Valores

```python
# Array cuyos valores son todos 1
np.ones((2, 3, 4))
```

- `np.ones((2, 3, 4))` - Crea un array de 2x3x4 lleno de unos.

```python
# Array cuyos valores son todos el valor indicado como segundo parámetro de la función
np.full((2, 3, 4), 8)
```

- `np.full((2, 3, 4), 8)` - Crea un array de 2x3x4 lleno del valor 8.

```python
# El resultado de np.empty no es predecible 
# Inicializa los valores del array con lo que haya en memoria en ese momento
np.empty((2, 3, 9))
```

- `np.empty((2, 3, 9))` - Crea un array de 2x3x9 con valores no inicializados.

### Inicialización con Arrays de Python

```python
# Inicializacion del array utilizando un array de Python
b = np.array([[1, 2, 3], [4, 5, 6]])
b
```

- `np.array([[1, 2, 3], [4, 5, 6]])` - Crea un array a partir de una lista de listas de Python.

### Inicialización con Funciones Basadas en Rangos

```python
# Creación del array utilizando una función basada en rangos
# (minimo, maximo, número elementos del array)
z = np.linspace(0, 6, 10)
z
```

- `np.linspace(0, 6, 10)` - Crea un array con 10 elementos equidistantes entre 0 y 6.

### Inicialización con Valores Aleatorios

```python
# Inicialización del array con valores aleatorios
np.random.rand(2, 3, 4)
```

- `np.random.rand(2, 3, 4)` - Crea un array de 2x3x4 con valores aleatorios entre 0 y 1.

```python
# Inicialización del array con valores aleatorios conforme a una distribución normal
np.random.randn(2, 4)
```

- `np.random.randn(2, 4)` - Crea un array de 2x4 con valores aleatorios de una distribución normal.

### Inicialización con Funciones Personalizadas

```python
# Inicialización del Array utilizando una función personalizada
def func(x, y):
    return x + 2 * y

np.fromfunction(func, (3, 5))
```

- `np.fromfunction(func, (3, 5))` - Crea un array de 3x5 utilizando la función [`func`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A474%2C%22character%22%3A9%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition").

---

## Acceso a los Elementos de un Array

### Array Unidimensional

```python
# Creación de un Array unidimensional
array_uni = np.array([1, 3, 5, 7, 9, 11])
print("Shape:", array_uni.shape)
print("Array_uni:", array_uni)
```

- `np.array([1, 3, 5, 7, 9, 11])` - Crea un array unidimensional.

```python
# Accediendo al quinto elemento del Array
array_uni[4]
```

- `array_uni[4]` - Accede al quinto elemento del array.

```python
# Accediendo al tercer y cuarto elemento del Array
array_uni[2:4]
```

- `array_uni[2:4]` - Accede al tercer y cuarto elemento del array.

```python
# Accediendo a los elementos 0, 3 y 5 del Array
array_uni[0::3]
```

- `array_uni[0::3]` - Accede a los elementos 0, 3 y 5 del array.

### Array Multidimensional

```python
# Creación de un Array multidimensional
array_multi = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Shape:", array_multi.shape)
print("Array_multi:\n", array_multi)
```

- `np.array([[1, 2, 3, 4], [5, 6, 7, 8]])` - Crea un array multidimensional.

```python
# Accediendo al cuarto elemento del Array
array_multi[0, 3]
```

- `array_multi[0, 3]` - Accede al cuarto elemento del array.

```python
# Accediendo a la segunda fila del Array
array_multi[1, :]
```

- `array_multi[1, :]` - Accede a la segunda fila del array.

```python
# Accediendo al tercer elemento de las dos primeras filas del Array
array_multi[0:2, 2]
```

- `array_multi[0:2, 2]` - Accede al tercer elemento de las dos primeras filas del array.

---

## Modificación de un Array

```python
# Creación de un Array unidimensional inicializado con el rango de elementos 0-27
array1 = np.arange(28)
print("Shape:", array1.shape)
print("Array 1:", array1)
```

- `np.arange(28)` - Crea un array unidimensional con valores del 0 al 27.

```python
# Cambiar las dimensiones del Array y sus longitudes
array1.shape = (7, 4)
print("Shape:", array1.shape)
print("Array 1:\n", array1)
```

- `array1.shape = (7, 4)` - Cambia la forma del array a 7x4.

```python
# El ejemplo anterior devuelve un nuevo Array que apunta a los mismos datos. 
# Importante: Modificaciones en un Array, modificaran el otro Array
array2 = array1.reshape(4, 7)
print("Shape:", array2.shape)
print("Array 2:\n", array2)
```

- `array1.reshape(4, 7)` - Devuelve un nuevo array con forma 4x7 apuntando a los mismos datos.

```python
# Modificación del nuevo Array devuelto
array2[0, 3] = 20
print("Array 2:\n", array2)
```

- `array2[0, 3] = 20` - Modifica el valor del cuarto elemento de la primera fila del array.

```python
print("Array 1:\n", array1)
```

- `print("Array 1:\n", array1)` - Muestra el array original para verificar que también ha sido modificado.

```python
# Desenvuelve el Array, devolviendo un nuevo Array de una sola dimension
# Importante: El nuevo array apunta a los mismos datos
print("Array 1:", array1.ravel())
```

- [`array1.ravel()`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A731%2C%22character%22%3A25%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition") - Devuelve un nuevo array unidimensional apuntando a los mismos datos.

---

## Operaciones Aritméticas con Arrays

```python
# Creación de dos Arrays unidimensionales
array1 = np.arange(2, 18, 2)
array2 = np.arange(8)
print("Array 1:", array1)
print("Array 2:", array2)
```

- [`np.arange(2, 18, 2)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A748%2C%22character%22%3A14%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition") - Crea un array con valores del 2 al 16 con un paso de 2.
- [`np.arange(8)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A749%2C%22character%22%3A14%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition") - Crea un array con valores del 0 al 7.

```python
# Suma
print(array1 + array2)
```

- [`array1 + array2`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A761%2C%22character%22%3A11%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition") - Suma los elementos de los dos arrays.

```python
# Resta
print(array1 - array2)
```

- [`array1 - array2`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A771%2C%22character%22%3A11%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition") - Resta los elementos de los dos arrays.

```python
# Multiplicacion
# Importante: No es una multiplicación de matrices
print(array1 * array2)
```

- [`array1 * array2`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A782%2C%22character%22%3A11%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition") - Multiplica los elementos de los dos arrays.

---

## Broadcasting

Si se aplican operaciones aritméticas sobre Arrays que no tienen la misma forma (shape), Numpy aplica una propiedad que se denomina Broadcasting.

```python
# Creación de dos Arrays unidimensionales
array1 = np.arange(5)
array2 = np.array([3])
print("Shape Array 1:", array1.shape)
print("Array 1:", array1)
print()
print("Shape Array 2:", array2.shape)
print("Array 2:", array2)
```

- [`np.arange(5)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A806%2C%22character%22%3A14%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition") - Crea un array con valores del 0 al 4.
- [`np.array([3])`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A807%2C%22character%22%3A14%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition") - Crea un array con un solo valor 3.

```python
# Suma de ambos Arrays
array1 + array2
```

- [`array1 + array2`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A761%2C%22character%22%3A11%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition") - Suma los elementos de los dos arrays aplicando broadcasting.

```python
# Creación de dos Arrays multidimensional y unidimensional
array1 = np.arange(6)
array1.shape = (2, 3)
array2 = np.arange(6, 18, 4)
print("Shape Array 1:", array1.shape)
print("Array 1:\n", array1)
print()
print("Shape Array 2:", array2.shape)
print("Array 2:", array2)
```

- [`np.arange(6)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A832%2C%22character%22%3A14%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition") - Crea un array con valores del 0 al 5.
- [`array1.shape = (2, 3)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A833%2C%22character%22%3A5%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition") - Cambia la forma del array a 2x3.
- [`np.arange(6, 18, 4)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A834%2C%22character%22%3A14%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition") - Crea un array con valores del 6 al 14 con un paso de 4.

```python
# Suma de ambos Arrays
array1 + array2
```

- [`array1 + array2`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A761%2C%22character%22%3A11%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition") - Suma los elementos de los dos arrays aplicando broadcasting.

---

## Funciones Estadísticas sobre Arrays

```python
# Creación de un Array unidimensional
array1 = np.arange(1, 20, 2)
print("Array 1:", array1)
```

- [`np.arange(1, 20, 2)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A866%2C%22character%22%3A14%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition") - Crea un array con valores del 1 al 19 con un paso de 2.

```python
# Media de los elementos del Array
array1.mean()
```

- [`array1.mean()`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A877%2C%22character%22%3A5%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition") - Calcula la media de los elementos del array.

```python
# Suma de los elementos del Array
array1.sum()
```

- [`array1.sum()`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A887%2C%22character%22%3A5%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition") - Calcula la suma de los elementos del array.

### Funciones Universales (ufunc)

Funciones universales eficientes proporcionadas por numpy.

```python
# Cuadrado de los elementos del Array
np.square(array1)
```

- [`np.square(array1)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A904%2C%22character%22%3A5%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition") - Calcula el cuadrado de los elementos del array.

```python
# Raiz cuadrada de los elementos del Array
np.sqrt(array1)
```

- [`np.sqrt(array1)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A914%2C%22character%22%3A5%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition") - Calcula la raíz cuadrada de los elementos del array.

```python
# Exponencial de los elementos del Array
np.exp(array1)
```

- [`np.exp(array1)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A924%2C%22character%22%3A5%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition") - Calcula el exponencial de los elementos del array.

```python
# log de los elementos del Array
np.log(array1)
```

- [`np.log(array1)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fg3n0s%2FDesktop%2FCursoDeep%2FIntroduccion%20a%20NumPy.ipynb%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A934%2C%22character%22%3A5%7D%7D%5D%2C%227bca7613-fb56-4d6d-b790-7565c9dc50b8%22%5D "Go to definition") - Calcula el logaritmo natural de los elementos del array.

---

## Recursos Adicionales

Para más información sobre NumPy, puedes consultar la [documentación oficial](https://numpy.org/doc/).

---

