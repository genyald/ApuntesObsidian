# Introducción a Pandas

#Pandas #Python

[Pandas](https://pandas.pydata.org/about/index.html) es una librería que proporciona estructuras de datos y herramientas de análisis de datos de alto rendimiento y fáciles de usar. La estructura de datos principal es el DataFrame, que puede considerarse como una tabla 2D en memoria (como una hoja de cálculo, con nombres de columna y etiquetas de fila). Muchas funciones disponibles en Excel están disponibles mediante programación, como crear tablas dinámicas, calcular columnas basadas en otras columnas, trazar gráficos, etc. Proporciona un alto rendimiento para manipular (unir, dividir, modificar…) grandes conjuntos de datos.

## Importación

```python
import pandas as pd
```

---

## Estructuras de datos en Pandas

La librería Pandas, de manera genérica, contiene las siguientes estructuras de datos:

- **Series**: Array de una dimensión
- **DataFrame**: Se corresponde con una tabla de 2 dimensiones
- **Panel**: Similar a un diccionario de DataFrames

### Creación del objeto Series

#### Creación de un objeto Series

```python
s = pd.Series([2, 4, 6, 8, 10])
print(s)
```

#### Inicialización con un diccionario de Python

```python
altura = {"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}
s = pd.Series(altura)
print(s)
```

#### Inicialización con algunos elementos de un diccionario de Python

```python
altura = {"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}
s = pd.Series(altura, index=["Pedro", "Julia"])
print(s)
```

#### Inicialización con un escalar

```python
s = pd.Series(34, ["test1", "test2", "test3"])
print(s)
```

---

## Acceso a los elementos de un objeto Series

Cada elemento en un objeto Series tiene un identificador único que se denomina **_index label_**.

### Acceso por etiqueta

```python
s = pd.Series([2, 4, 6, 8], index=["num1", "num2", "num3", "num4"])
print(s)
s["num3"]
```

> [!warning] `Esto es una mala práctica, lo correcto es hacer uso de s.loc['num3']:`

```python
s.loc["num3"]
```

### Acceso por posición

```python
s[2]
```

> [!warning] `Esto es una mala práctica, lo correcto es usar s.iloc[2]:`
> ```python
>s.iloc[2]
>```

Por segmentación: 

```python
s.iloc[2:4]
```

---

## Operaciones aritméticas con Series

### Creación de un objeto Series

```python
s = pd.Series([2, 4, 6, 8, 10])
print(s)
```

### Compatibilidad con Arrays de Numpy

```python
import numpy as np
np.sum(s)
```

### Otras operaciones aritméticas

```python
s * 2
```

---

## Representación gráfica de un objeto Series

### Creación de un objeto Series denominado Temperaturas

```python
temperaturas = [4.4, 5.1, 6.1, 6.2, 6.1, 6.1, 5.7, 5.2, 4.7, 4.1, 3.9]
s = pd.Series(temperaturas, name="Temperaturas")
s
```

### Representación gráfica del objeto Series

```python
%matplotlib inline
import matplotlib.pyplot as plt

s.plot()
plt.show()
```

---

## Creación de un objeto DataFrame

### Inicialización con un diccionario de objetos Series

```python
personas = {
    "peso": pd.Series([84, 90, 56, 64], ["Santiago", "Pedro", "Ana", "Julia"]),
    "altura": pd.Series({"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}),
    "hijos": pd.Series([2, 3], ["Pedro", "Julia"])
}

df = pd.DataFrame(personas)
df
```

### Forzar columnas y orden específico

```python
df = pd.DataFrame(
    personas,
    columns=["altura", "peso"],
    index=["Ana", "Julia", "Santiago"]
)
df
```

### Inicialización con una lista de listas de Python

```python
valores = [
    [185, 4, 76],
    [170, 0, 65],
    [190, 1, 89]
]

df = pd.DataFrame(
    valores,
    columns=["altura", "hijos", "peso"],
    index=["Pedro", "Ana", "Juan"]
)
df
```

### Inicialización con un diccionario de Python

```python
personas = {
    "altura": {"Santiago": 187, "Pedro": 178, "Julia": 170, "Ana": 165}, 
    "peso": {"Santiago": 87, "Pedro": 78, "Julia": 70, "Ana": 65}
}

df = pd.DataFrame(personas)
df
```

---

## Acceso a los elementos de un DataFrame

### Acceso a las columnas del DataFrame

```python
df["peso"]
```

```python
df[["peso", "altura"]]
```

#### Combinación con expresiones booleanas

```python
df[df["peso"] > 80]
```

```python
df[(df["peso"] > 80) & (df["altura"] > 180)]
```

### Acceso a las filas del DataFrame

```python
df.loc["Pedro"]
```

```python
df.iloc[2]
```

```python
df.iloc[1:3]
```

---

## Consulta avanzada de los elementos de un DataFrame

```python
df.query("altura >= 170 and peso > 60")
```

---

## Copiar un DataFrame

```python
df_copy = df.copy()
df_copy
```

> [!info] `Al modificar un elemento de df_copy no se modifica df.`

---

## Modificación de un DataFrame

### Añadir una nueva columna

```python
df["cumpleaños"] = [1990, 1987, 1980, 1994]
df
```

### Añadir una nueva columna calculada

```python
df["años"] = 2024 - df["cumpleaños"]
df
```

### Añadir una nueva columna creando un DataFrame nuevo

```python
df_mod = df.assign(mascotas = [1, 3, 0, 0])
df_mod
```

### Eliminar una columna existente

```python
del df["peso"]
df
```

### Eliminar una columna devolviendo una copia del DataFrame resultante

```python
df_mod = df.drop(["hijos"], axis=1)
df_mod
```

---

## Evaluación de expresiones sobre un DataFrame

### Evaluar una función sobre una columna

```python
df.eval("altura / 2")
```

### Asignar el valor resultante como una nueva columna

```python
df.eval("media_altura = altura / 2", inplace=True)
df
```

### Evaluar una función utilizando una variable local

```python
max_altura = 180
df.eval("altura > @max_altura")
```

### Aplicar una función externa a una columna

```python
def func(x):
    return x + 2

df["peso"].apply(func)
```

---

## Guardar y Cargar el DataFrame

### Guardar el DataFrame

```python
df.to_csv("df_personas.csv")
df.to_json("df_personas.json")
```

### Cargar el DataFrame

```python
df2 = pd.read_json("df_personas.json")
df2
```

---

## Recursos Adicionales

- [Documentación oficial de Pandas](https://pandas.pydata.org/pandas-docs/stable/)
- [Tutoriales de Pandas en W3Schools](https://www.w3schools.com/python/pandas/default.asp)

---

## Información Adicional

Pandas es una herramienta poderosa para la manipulación y análisis de datos. Su integración con otras librerías como NumPy y Matplotlib la hace indispensable para el análisis de datos en Python.