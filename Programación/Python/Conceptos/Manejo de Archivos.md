#Python #Files 

Consultar [[Manejo de Contexto `with`|Context Manager]].

En python nativamente podemos hacer manejo de cierto tipo de archivos con sus respectivas extensiones de manera nativa, estos son:

- `.txt`
- `.csv`
- `.json`
- `.xml`
- `.cfg`
- `.ini`
- `.bin`

Sin embargo, con su respectiva bibloteca *podemos trabajar con cualquier tipo de archivo en python*.
### Archivos tipo txt

Para abrir de forma automatica o *crearlo si hace falta*, podemos hacer uso de la `funcion` `open()`, inclusive para escribir informacion a un archivo.

A veces puede arrojar un error, por lo que es comun ponerlo en un `try/catch`:

```python
try:
	archivo = open('prueba.txt', 'w', encoding = 'utf8')
	archivo.write('Agregamos informacion al archivo')
	archivo.write('\nAdios')
except Exception as e:
	print(e)
finally:
	archivo.close()
```

>El [[Manejo de Contexto `with`|Context Manager]] puede simplificar el `archivo.close` con el simple uso de `with`.
### Uso de `open()`

```python
file = open('ruta/del/archivo', 'modo')
```
#### Modos de Apertura

- `'r'` : Lectura (modo por defecto). El archivo debe existir.
- `'w'` : Escritura. Crea un nuevo archivo o sobrescribe el existente.
- `'a'` : Añadir. Escribe al final del archivo sin borrar el contenido existente. Si no lo crea.
- `'b'` : Modo binario. Se usa junto con otros modos (e.g., `'rb'` o `'wb'`).
- `'t'` : Modo texto (modo por defecto). Se usa junto con otros modos `'rt'` o `'wt'`.
- `'x'`: Crear. Crea el archivo especifico, si existe regresa un error.
- `'+'` : Lectura y escritura. Se usa junto con otros modos (e.g., `'r+'` o `'w+'`).

- Abrir un Archivo:

```python
archivo = open('prueba.txt', 'r', encoding = 'utf8')
```

- Leer todo el contenido del archivo:
```python
archivo = open('prueba.txt', 'r', encoding = 'utf8')
contenido = archivo.read()
print(contenido)
```

- Leer una línea del archivo:
```python
linea = archivo.readline()
print(linea)
```

- Leer todas las líneas del archivo (`lineas` se vuelven lista):
```python
lineas = archivo.readlines()
print(lineas)
```

- Acceder a una linea especifica:
```python
lineas = archivo.readlines()
print(lineas[3])
```
- Escribir en un archivo (modo escritura):
```python
file = open('prueba.txt', 'w', encoding = 'utf8')
file.write('Texto a escribir\n')
```

- Añadir texto a un archivo (modo añadir):
```python
file = open('prueba.txt', 'a', encoding = 'utf8')
file.write('Texto añadido\n')
```

- Abrir un archivo en modo binario para lectura:
```python
file = open('prueba.bin', 'rb')
contenido_binario = file.read()
```

- Abrir un archivo en modo binario para escritura:
```python
file = open('prueba.bin', 'wb')
file.write(b'Datos binarios')
```

- Iterar nuestro archivo (Esto es porque se recupera como lista cada linea):
```python
archivo = open('prueba.txt', 'r', encoding = 'utf8')
for linea in archivo:
	print(linea)
```

- Hacer una copia de nuestro archivo:
```python
archivo = open('prueba.txt', 'r', encoding = 'utf8')
copia = open('copia.txt', 'w', encoding = 'utf8')
contenido_archivo = archivo.read()
copia.write(contenido_archivo)
print(contenido_archivo)

copia.close()
archivo.close()
```

- Cerrar el archivo:
```python
file.close()
```


> [!quote] `with`
> ![[Manejo de Contexto `with`]]



Leer algunos caracteres del archivo:

```python
# Leer los primeros 8
archivo = open('prueba.txt', 'r', encoding = 'utf8')
print(archivo.read(8), end = '')
# Leer los siguientes 13
print(archivo.read(13))
```


> [!NOTE] `archivo.read()`
> Si se quiere leer una parte especifica del codigo, es necesario no haber usado `archivo.read()` debido a que ese comando lee todo el archivo de texto, necesitamos usarlo pero especificando la cantidad de caracteres a leer:
> ```python
> archivo = open('prueba.txt', 'r', encoding = 'utf8')
> print(archivo.read(5))
>```

> [!question] `encoding = 'utf8`
> **UTF-8 (Unicode Transformation Format - 8-bit)** es un estándar de codificación de caracteres ampliamente utilizado debido a su compatibilidad con ASCII y su eficiencia. Tiene las siguientes características:
>- **Compatibilidad con ASCII**: Los caracteres ASCII (U+0000 a U+007F) se representan con un solo byte.
>- **Codificación Variable**: Usa de 1 a 4 bytes para representar caracteres, optimizando el uso del espacio.
>- **Auto-sincronización**: Permite determinar el inicio de un carácter en una secuencia de bytes, facilitando la búsqueda y corrección de errores.
>- **Compatibilidad Internacional**: Puede representar cualquier carácter de cualquier idioma, ideal para aplicaciones globales.


> [!important] Abrir o especificar una ruta en especifico
> En windows, cuando especificicamos la ruta especifica del archivo, debemos usar doble diagonal inversa para especificar una diagonal, ya que `\` es un caracter que significa escape y sirve para indicar tabulacion, salto del linea, etc. Por lo que debemos usar `\\` para especificar que es un caracter especial:
> ```python
> archivo = open('C:\\Users\\genya\\AppData\\Local\\Programs\\obsidian\\prueba.txt', 'r', encoding = 'utf8')
> print(archivo.read())
>```
