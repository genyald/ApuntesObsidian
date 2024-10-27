#Python #Strings

Es un tipo de dato el cual es una secuencia de caracteres. En python las cadenas pueden ser definidas usando comillas simples, comillas dobles o comillas triples dobles.

## Acceso a caracteres y subcaracteres

*Se puede accedes a caracteres individuales y subcadenas usando indices y slices:*

### Acceso a un caracter
```python
str1 = 'Hola Mundo'
primer_caracter = str1[0]
ultimo_caracter = str1[-1]
print(primer_caracter, ultimo_caracter)
```

Esto se debe a que se enumeran de cero en adelante pero al reves se enumeran desde el -1 hacia atras.

### Acceso a una subcadena

```python
sub_str = str1[1:4]
print(sub_str)
```

## Métodos Comúnes de Cadenas

- `.lower()` y `.upper()`: Convierten una cadena en minusculas o en mayusculas:
```python
minusculas = str1.lower()
mayusculas = str1.upper()
print(minusculas, mayusculas)
```

- `.strip('str')` - Elimina `str` al inicio y final de una cadena, por defecto el espacio.
- `.lstrip('str')` - Elimina los `str` al inicio de una cadena, por defecto el espacio.
- `.rstip('str')` - Elimina `str` al final de una cadena, por defecto el espacio.
```python
string = ' Hola mundo '
no_space = string.strip()
left_nospace = string.lstrip()
right_nospace = string.rstrip()
print(string)
print(no_space)
print(left_nospace)
print(right_nospace)
```

>`strip` se puede usar varias veces al mismo texto para procesarlo/limpiarlo.


- `.split()` convierte una cadena en una lista con un delimitador (espacio por defecto): 
```python
string = 'Hola Mundo'
lista = string.split(' ')
print(lista)
```

- Podemos agregar el parametro de `maxsplit`, el cual delimita la cantidad de cadenas que contendra nuestra lista:
```python
string = 'El perrito que se llamaba pegamento se cayo y se pego'
lista = string.split(' ', 3)
print(lista)
```

- `.join()`: Convierte una lista en una cadena e inserta un caracter entre ellas:

1. Con listas:
```python
lista = ['Hola', 'Mundo', 'Geny', 'Ochoa']
print(lista)
cadena = ' '.join(lista) # ' ' es lo que se inserta entre cada lista
print(cadena)
cadena2 = '.'.join(lista)
print(cadena2)
```

2. Con cadenas también:

```python
cadena = 'Hola'
cadena3 = '.'.join(cadena)
print(cadena3)
```

3. Con diccionarios:
```python
diccionario = {'nombre': 'Geny', 'apellido': 'Ochoa', 'edad': '23'}
llaves = '-'.join(diccionario.keys())
valores = ' '.join(diccionario.values())
print(f'{llaves}: tipo: {type(llaves)}')
print(f'{valores}: tipo: {type(valores)}')
```

- `.replace()`: Remplaza una subcadena/contenido por otr@:
```python
string = 'Hola Mundo'
new_string = string.replace('Mundo', 'Python') # dato.replace('A remplazar', 'Remplazo')
print(string)
print(new_string)
```

- `.find()` y `.rfind()`: Encuentran la posición de una subcadena:
```python
pos = string.find('Mundo')
last_pos = string.rfind('o') # Encontrara la posicion de la ultima o
print(pos, last_pos)
```

- `.startswith()` y `.endswith()`: Verifica si una cadena comienza o termina con una subcadena:
```python
cadena = "Hola Mundo"
empieza_con = cadena.startswith("Hola")  # True
termina_con = cadena.endswith("Mundo")  # True
print(empieza_con, termina_con)
```

- `capitalize()` convierte en mayuscula la primer letra de la cadena y el resto la devuelve en minuscula.
```python
cadena = 'hola Mundo'
cadena = cadena.capitalize()
print(cadena)
```


> [!warning] INMUTABLES
> Realmente, los `str` en python son inmutables, cada vez que lo modificamos, se crea un nuevo objeto `str` con las modificaciones, no se afecta realmente a la cadena original.
> ```run-python
> mensaje1 = 'Hola a todos'
> print(hex(id(mensaje1)))
>
>mensaje1 = mensaje1.upper()
> print(hex(id(mensaje1)))
> ```
> Como se puede ver, a pesar de que la variable sigue siendo la misma, ahora la literal ha cambiado a una con nuestro nuevo `str`.


## Formateo de Cadenas

#Formato

Python ofrece varias formas de formatear cadenas:
### **Operador `%`** (Parametro posicional, como en C):

```python
nombre = 'Juan'
edad = 30
cadena_formateada = 'Mi nombre es %s y tengo %d años' % (nombre, edad)
print(cadena_formateada)
```

- **`%s`**: String (cadena de caracteres)
- **`%d`**: Integer (entero)
- **`%i`**: Integer (entero)
- **`%f`**: Float (número de punto flotante)
- **`%e`**: Scientific notation (notación científica)
- **`%g`**: General format (formato general, utiliza `%f` o `%e`)
- **`%x`**: Hexadecimal (base 16, letras minúsculas)
- **`%X`**: Hexadecimal (base 16, letras mayúsculas)
- **`%o`**: Octal (base 8)

```python
persona = ('Karla', 'Gomez', 50000.0005)
mensaje_formateado = 'Hola %s %s, tu sueldo es de %.2f'%persona
print(mensaje_formateado)
```

>Tambien podriamos asignarle los valores a la hora de imprimirlo:

```python
mensaje_formateado = 'Hola %s %s, tu sueldo es de %.2f'
print(mensaje_formateado%persona)
```

### Por comas:
```python
nombre = 'Juan'
edad = 25
print('Mi nombre es:', nombre, 'Y tengo:', edad)
# Sin el print:
frase = 'Mi nombre es:', nombre, 'Y tengo:', edad
print(frase)
```

### Método Format

>El metodo `format()` hace que las llaves `{}` conocidas como `placeholders` sean elementos que serán remplazados.
```python
nombre = 'Juan'
edad = 28
sueldo = 20000.005

cadena_formateada = 'Nombre: {}, Edad: {}, Sueldo: {:.2f}'.format(nombre, edad, sueldo)

print(cadena_formateada)
```

Tambien podemos hacerlo indicando la posicion de los elementos (como en los datos de tipo secuencia):

```python
mensaje = 'Nombre: {0}, Edad: {1}, Sueldo: {2:.2f}'.format(nombre, edad, sueldo)
print(mensaje)
```

Como ahora cuentan con su respectivo indice los valores, podemos manejarlos libremente en el formateo:

```python
mensaje = 'Sueldo: {2:.2f}, Edad: {1}, Nombre: {0}, Sueldo de nuevo: {2:.2f}'.format(nombre, edad, sueldo)
print(mensaje)
```

- Otra forma de especificar los valores es usando nombres y argumentos:

```python
mensaje = 'Nombre: {n}, Edad: {e}, Sueldo: {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
print(mensaje)
```

Esto tiene la ventaja de ahorrarnos lineas de codigo para declarar los valores del formato.

- Finalmente, podemos hacer uso de diccionarios:
```python
diccionario = {'nombre': 'Ivan', 'edad':43, 'sueldo':80000.000}
mensaje = 'Nombre: {dicc[nombre]}, Edad: {dicc[edad]}, Sueldo: {dicc[sueldo]:.2f}'.format(dicc=diccionario)
print(mensaje)
```
### **F-strings** o Template Literal (nuevo en Python 3.6+): ^format

```python
cadena_formateada = f'Nombre: {nombre}, Edad: {edad}, Sueldo: {sueldo:.2f}'
print(cadena_formateada)
```

Cuando ponemos una expresion o variable en un placeholder se le conoce como interpolación. La ventaja de esto es que inclusive podemos mandar a llamar una función en el placeholder.


> [!summary] `print()` tiene un leve formateo:
> Podemos hacer uso de argumentos extra para darle formato al print, estos son sus argumentos con un ejemplo:
> ```python
> print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
> ```
> - **`*objects`**: Objetos a imprimir (separados por comas).
>- **`sep`**: Separador entre objetos (por defecto es un espacio `' '`).
>- **`end`**: Lo que se añade al final (por defecto es un salto de línea `'\n'`).
>- **`file`**: Flujo de salida (por defecto es `sys.stdout`).
>- **`flush`**: Forzar el vaciado del buffer (por defecto es `False`). ^print


También podemos usar docstrings (`'''`) para indicar que nuestro f-string consta de varias líneas:
```python
print(f'''
Hola
Cara de Bola
Jejeje
''')
```

> [!info] Forma no tan conocida
> Como ya se sabe, se pueden concatenar cadenas con `+`, sin embargo, tambien se pueden concatenar omitiendo esta misma:
> ```python
>variable = 'Hola' + 'Mundo'
>print(variable)
>
>variable =  'Hola' 'Mundo'
>print(variable)
>
>mensaje = 'Geny ' 'Aldair'
>mensaje += 'Ochoa' 'Romero'
>print(mensaje)
>```
>Asi mismo, como se observa se puede hacer uso de `+=` para sumarle algo a una cadena.
## Especificadores de Formato

### Alineación

- **Alinear a la derecha**: `>`
- **Alinear a la izquierda**: `<`
- **Alinear al centro**: `^`

```python
valor = 123.456
valor1 = 123
print(f'{valor:>10.2f}')  # Alineado a la derecha en un campo de 10 caracteres
print(f'{valor:<10.2f}')  # Alineado a la izquierda en un campo de 10 caracteres
print(f'{valor:^10.2f}')  # Alineado al centro en un campo de 10 caracteres
print(f'{valor1:^10x}')
```

- Para _alinear al centro_ de un `print` hacemos uso de `.center(largo, caracter)`:

```python
titulo = 'Programa que dice Hola :0'
print(titulo.center(len(titulo)+10, '-'))
```

En este print tomamos el largo de la cadena y le sumamos 10 para que sean los caracteres insertados a los lados, el caracter a insertar es `'-'`.

- Para _alinear a la izquierda_ hacemos uso de `ljust(largo, caracter)`:
```python
titulo = 'Programa que dice Hola :0'
print(titulo.ljust(len(titulo)+10, '-'))
```

En este print tomamos el largo de la cadena y le sumamos 10 para que sean los caracteres insertados a la dercha, el caracter a insertar es `'-'`.

- Para _alinear a la derecha_ hacemos uso de `rjust(largo, caracter)`:
```python
titulo = 'Programa que dice Hola :0'
print(titulo.rjust(len(titulo)+10, '-'))
```

En este print tomamos el largo de la cadena y le sumamos 10 para que sean los caracteres insertados a la izquierda, el caracter a insertar es `'-'`.


> [!INFO] Para Usar la Alineacion
> Para que el metodo aplicado para la alineacion, el largo de los caracteres debe superar el que le demos de parámetros, de lo contrario no hará ninguna alineación.

### Ancho del Campo

El ancho del campo especifica el número mínimo de caracteres que ocupará la expresión formateada.

```python
valor = 123.456
print(f'{valor:10.2f}')  # Campo de 10 caracteres, con 2 decimales
```
### Precisión

La precisión se especifica después de un punto (`.`) y determina el número de decimales para números de punto flotante.

```python
valor = 123.456
print(f'{valor:.2f}')  # 2 decimales
```

### Concatenación

La concatenación es la unión de cadenas de texto, se puede usar el operado `+`:

```python
str1 = 'Hola'
str2 = 'Mundo'
full_str = str1 + ' ' + str2 # El ' ' es el caracter del espacio
variable = 'Estoy haciendo un ' + str1 + ' ' + str2 + ' en Python'
print(full_str)
print(variable)
```

### Repetición Por Multiplicacion

Puedes repetir una cadena de texto una n veces usando el operador `*`:
```run-py
str1 = 'Hola'
str1_rep = str1 * 3 # HolaHolaHola
print(str1_rep)
```
Inclusive podemos hacerlo con tuplas:

```python
resultado = 5*('Hola',)
print(resultado)

resultado = 7*('Hola', 'Mundo')
print(resultado)

# Con tupla de numeros
resultado = 3*(1,2,3)
print(resultado)
```
Con listas (creamos una lista de 0's con 10 de largo):

```python
resultado = 10*[0]
print(resultado)
```
### Longitud

Podemos obtener la longitud de una cadena con la funcion `len()`:

```run-py
str1 = 'Hola Mundo'
print(len(str1))
```

### Caracteres de Escape

Son caracteres que estan dentro de una cadena que causan que se ejecute una accion fuera del texto, normalmente se puede usar para usar caracteres especiales:
```python
resultado = 'Hola\' Mundo'
print(resultado)
```

Un ejemplo de ellos es el backspace: (Visualizar en VSCode)

```python
resultado = 'Se va a eliminar el punto.\b '
print(resultado)
```

Para poner `\` debemos poner el caracter de escape seguido de la diagonal inversa (`\\`):

```python
resultado = 'c:\\dir\\nuevo\\juan'
print(resultado)
```

Si no usasemos `\\` se reonoceria `\n` de `\nuevo` y haria un retorno de linea.

>Para evitar todo esto podemos hacer uso de `raw string` (`r'string'`): ^rawstring

```python
directorio = r'D:\Users\genya\Documentos'
print(directorio)
```

## Caracteres Unicode y ASCCI

#Unicode #ASCCI

### Unicode
Es un set de caracteres universal, es decir, un estándar en el que se definen todos los caracteres necesarios para la escritura de la mayoria de los idiomas hablados en la actualidad que se usan en la computadora.

Tiene la característica de usar UTF-8, UTF-16 o UTF-32, lo que significa que sus posibles combinaciones son suficientes para representar todos los caracteres hechos por el humano, aunque se actualiza constantemente.

Todos los caracteres en python se representan con el juego de caracteres unicode. Por ejemplo, la letra `A` tiene un valor de `41` o en decimal de `65`, por defecto estan en hexadecimal, cuando se usa `U+0041`. El `U+` se refiere a los ceros faltantes para ser ocho.

Para hacer uso de un caracter unicode en python podemos hacer uso de `\u0000`:

```python
print(u'Hola\u0020Mundo')
print('Notacion simple: (\\u)', '\u0041')

# Notacion extendida (8 valores Hexa)
print('Notacion extendida: (\\U)', '\U00000041')

# Notacion simplificada (Maximo 2 valores de unicode)
print('Notacion simplificada: (\\x)', '\x41')
```

(En versiones anteriores de python se requeria el prefijo 'u', actualmente no es necesario).

>Una de las principales ventajas de hacer uso de unicode es que podemos utilizar iconos: 

```python
print('Corazon: ', '\u2665')
print('Cara sonriendo:', '\U0001F604')
```

### ASCII

Por sus siglas: _American Standard Code for Information Interchange_, podemos trabjar con ellos tal como lo hacemos con unicode, la unica desventaja es que no cuenta con el numero tan extenso de caracteres, sin embargo es util cuando nuestra interface no cuenta con todos los caracteres unicode en su sistema.

Por ejemplo, la letra `A` segun la tabla de ASCII, tiene el valor decimal de `65`, para representar en python:

```python
# Caracter ASCII
caracter = chr(65)
print('A mayuscula:', caracter)
# En Hexadecimal
caracter = chr(0x61)
print('A minuscula:', caracter)
# En Octal
caracter = chr(0o100)
print('Arroba:', caracter)
```

Estos temas son importantes para poder convertir valores unicode y ascii que recibimos para ser procesados.

## Manejo de Literales Tipo Byte

Cuando trabajamos con informacion obtenida directamente de la red no recibimos la informacion convertida, por lo que hay que saber procesar los bits/bytes recibidos para que le demos un debido procesamiento. Para trabajar con literales de tipo byte hacemos uso del prefijo `b`:

```python
caracteres_bytes = b'Hola Mundo'
print(caracteres_bytes)
```

Siendo similar a los string, igual podemos trabjar con ellos como indices:

```python
print(caracteres_bytes[0])
```

La diferencia aqui es que en lugar de habernos devuelto la letra `H`, nos ha devuelto el valor decimal ASCII de la letra `H` -> `72`. 

Podemos usar el metodo `chr()` para saber a la letra que pertenece en la tabla ASCII:

```python
print(chr(caracteres_bytes[0]))
```

Le podemos aplicar el metodo `.split()` para convertirlo en una lista, sin embargo esta sera del tipo byte:

```python
caracteres = caracteres_bytes.split()
print(caracteres)
```

Gracias el prefijo de `b` sabemos que no son unicode si no tipo `byte`.

### Convertir Str a Bytes y Viceversa

Para convertir de string a bytes hacemos uso del metodo `.encode()` con el metodo de transformacion a usar con los bytes, en este caso, UTF-8:

```python
# De string a bytes
string = 'Programación con python'
print('String original:', string)
bytes = string.encode('UTF-16') # Por defecto se maneja UTF-8
print('Bytes codificados:', bytes)
```

Como se puede apreciar, el print no codifica el acento, para ello deberiamos codificar el texto en bytes para poder imprimirlo/procesarlo correctamente:

```python
# De bytes a string
string2 = bytes.decode('UTF-16')
print('String decodificado:', string2)
```

Podemos comprobar si la cadena original es igual a la cadena decodificada:

```python
print(string == string2)
```

> [!info] UTF-8
> Viene de las iniciales _Unicode Transformation Format_ y la ventaja es que es compatible con ASCII, por lo que cualquier texto codificado en ASCII tambien es unicode valido. ASCII usa solo siete bits, cuando usa 8 se le conoce como Extended ASCII. Unicode es, digamos la continuación de ASCII. Actualmente, UTF-16 es el estándar de transmisión de información por internet.

## Metodos Adicionales

Contamos con el metodo `count()`, el cual nos devolvera el numero de veces que aparece el parametro entregado en el texto:

>Para el ejemplo usaremos el ejercicio: [[Leer Contenido Online]].

```python
from urllib.request import urlopen, Request

url = 'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'}

# Hacemos un request del URL
request = Request(url, headers=headers)
lista = []

# Abrimos el url con el request
with urlopen(request) as mensaje:
    contenido = mensaje.read().decode('utf8')
    print('Numero de veces de \'Universidad:\'',  contenido.count('Universidad'))
```

- Usar `.lower()` y `.upper()` para hacer comparaciones acertadas:
```python
print('"python" esta en el contenido:','python' in contenido)
contenido_mayus = contenido.lower()
print('"python" esta en el contenido:','python' in contenido_mayus)
```

### Metodos Adicionales Rapidos:

- `.starstwith('str')` : Devuelve `True` si el contenido _empieza_ con el `str`. 
- `.endswith('str')`: Devuelve `True` si el contenido _termina_ con el `str`.
-  `.islower('str')`: Devuelve `True` si **todo** el `str` esta en _minusculas_.
- `.isupper('str')`: Devuelve `True` si **todo** el `str` esta en _mayusculas_.