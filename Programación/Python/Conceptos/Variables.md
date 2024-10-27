#Python #Vars

Las variables se almacenan en una dirección de memoria `RAM` de la `PVM`. **Los valores que asignamos a nuestra variable es una literal.** ^literal

```python
x = 10
y = 2
z = x + y
print(z)
```

En la memoria se veria tal que:

| x -> | **10** |
| ---- | :----: |
| y -> | **2**  |
| z -> |   12   |
Las variables, apuntan a la dirección de memoria donde se encuentra la literal, la literal es el dato al que apunta nuestra variable. ^literalyvariable

Para saber que direccion de memoria tiene una literal podemos usar la funcion 'id' y la variable que apunta a esa literal:

```python
# Para llamar a la direccion de memoria:
id(x)
# Para visualizarlo en cosola:
print('{:x}'.format(id(x)))
```

## Verificar si una variable existe

Podemos verificar con un `if` si una variable existe, esto nos sirve inclusive para saber si un objeto esta creado, la sintaxis es la siguiente:

```python
variable = 100
if variable:
	print('Si existe "variable"')
```

## Palabras Reservadas (keywords)

#ReservatedString

Para conocer todas las palabras reservadas o `keywords` en python, podemos hacer uso de `import keyword` y para imprimir todas las palabras reservadas usamos `keyword.kwlist`:

```python
import keyword
print(keyword.kwlist)
```

Estas `keywords` no pueden ser usadas como `variables/funciones/clases/archivos` o obtendremos un error de sintaxis:

```python
as = 'Hola'
```
