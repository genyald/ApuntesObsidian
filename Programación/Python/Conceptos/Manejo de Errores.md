#Python #TryExcept

Un error o una excepción en python es cuando nuestro programa termina de forma abrupta, o nos devuelve un error. Todo el manejo de errores vienen de las siguientes clases heredadas nativamente en el lenguaje:

![[manejo-errores.png]]

Para lo mas básico del manejo de excepciones:

```python
try:
	asldkj
except Exception as e:
	print(f'Ocurrio un error: {e}')
```

Podemos capturar una excepcion mas especifica y modificar el comportamiento del codigo cuando esto pase:

```python
try:
	10/0
except ZeroDivisionError as e:
	print(f'Error aritmetico {e}')
```

O al controlar directamente este error podemos cambiar el mensaje para este caso especifico:

```python
try:
	10/0
except ZeroDivisionError:
	print('Error de division por cero')
```

Eso significa que podemos capturar la excepción con una clase padre o con una mas especifica. Lo recomendable es hacer excepciones lo mas generales posibles, a menos que sea un caso de aplicación muy puntual.

> [!important] En otros lenguajes `try/except` se conocoe como `try/catch`

Usando algunas literales para procesar este codigo:

```python
resultado = None
a = '10'
b = 0
try:
	resultado = a/b
except TypeError as e:
	print(f'Ocurrrio un error del Tipo {type(e)}')
	
print(f'Resultado {resultado}')
print('Continuamos')
```

Cuando un bloque try no se ejecuta exitosamente, este omite toda esa seccion de código, como si no estuviese.

Si queremos procesar las excepciones mas especificas:
```python
try:
	resultado = a/b
except ZeroDivisionError as e:
	print(f'Ocurrio un error de division por cero {type(e)}')
except TypeError as e:
	print(f'Ocurrio un error: {type(e)}')
	
print(f'Resultado {resultado}')
```


> [!info] Excepcion `Except`
> Si se usa `Except` en varios `except`, debe ser al final para que se validen los anteriores primero o se omitiran. Osea perimero se deben usar las clases de mas alto nivel.

## Bloques Adicionales

#Finally #BloquesAdicionales

Contamos con el bloque `else` y el bloque `finally`, el bloque else se ejecuta cuando **no se ha lanzado ninguna excepcion** y todo sale como se espera. El bloque `finally` **siempre se va a ejecutar habiendo una excepcion o no**.

```python
resultado = None
try:
	a = int(input('Dame el valor "a": '))
	b = int(input('Dame el valor "b": '))
	resultado = a + b
except ValueError as e:
	print(f'Error del tipo ValueError: {type(e)}')
else:
	print('Ejecucion del bloque else')
finally:
	print('Ejecucion del bloque finally')

print('Resultado de la suma: ' + str(resultado))
# del a, b
```

## Definir Excepciones Propias

#Raise

Como se aprecia en la imagen [[manejo-errores.png]], todas las excepciones vienen de la clase padre `Exception`, sin embargo podemos definir nuestras propias excepciones para la personalizacion de los errores en nuestro código.

Para crear la excepcion personalizada, basta con heredar de Exception e inicializar el atributo `messaje`, el cual se le da al inicializar el objeto:

```python
class NumerosIdenticos(Exception):
	def __init__(self, mensaje):
		self.messaje = mensaje
```

Aqui esta creada nuestra propia excepcion, solo basta con hacer uso de la palabra reservada `raise` para lanzar nuestras propias excepciones:

```python
a = 5
b = 5
if a == b:
	raise NumerosIdenticos('Numeros identicos')
```


> [!summary] `raise`
> Raise se usa para arrojar cualquier tipo de excepcion que este presente en una clase del tipo `Exception`, por lo que podemos mandar a llamar cualquiera, como: `raise ValueType` y mandara a llamar este tipo de error. Por lo que no es solo para excepciones personalizadas.


