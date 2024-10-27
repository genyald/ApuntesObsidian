#Python #Vars #Global #Local

El Alcanze de Variables, tambien conocido como `scope` es el dominio en el que puede ser usada una variable, una variable en python puede ser accedida desde bloques de codigo mas interno, pero puede ser accedida desde bloques mas externos.

Una variable declarada el archivo principal o en el `main` sera una variable que puede ser usada en todos lados, ya que no hay un nivel mas alto, este tipo de variables son conocidas como _variables globales_. ^variableglobal

```python
var_global = 'Variable Global'

def imprimir():
	print(f'Variable global accedida desde una funcion: {var_global}')

imprimir()
```

El `scope` de una variable definida dentro de un bloque de codigo, es solamente este mismo, no se pude llamar desde fuera, a este tipo de variables se les conoce como _variables locales_.

```python
def imprimir():
	var_local = 'Variable Local'
	print('Variable Local accedida desde la funcion:', var_local)

imprimir()
```

Una variable local puede ser accedida dentro de bloques mas internos, sin embargo no se puede a bloques mas externos.

```python
def imprimir():
	var_local = 'Variable Local'

try:
	print(var_local)
except Exception:
	print('No se puede acceder a la variable')
```


> [!WARNING] Modificar e Imprimir una Variable Global Dentro de un Bloque de Codigo
> Cuando llamamos una variable global dentro de bloque de codigo, esta se considera como lectura y por lo tanto al intentar modificarla estamos sobrescriviendola con una local, para evitar eso hacemos uso de la palabra reservada `global`, esto nos deja modificarla y acceder a ella: ^modificarGlobal
> - Con error:
> ```python
> var_global = 'Variable Global'
> def imprimir():
> 	print(var_global)
> 	var_global = 'Modificada la variable global'
> 	print(var_global)
> imprimir()
>```
>- Sin error:
>```run-python
>var_global = 'Variable Global'
> def imprimir():
> 	global var_global
> 	print(var_global)
> 	var_global = 'Modificada la variable global'
> 	print(var_global)
> imprimir()
>```


## Alcance de Variables y Funciones Anidadas

Podemos combinar el concepto de [[Alcanze de Variables]] y [[Funciones#Funciones Anidadas|Funciones Anidadas]], ya que podemos acceder a la variable de nivel mas alto en cuanto una funcion anidada, pero ¿Cómo le decimos al programa que no es una variable local de esa funcion? Para ello hacemos uso de `nonlocal`.

```python
def funcion_externa():
	variable_local_externa = 'Variable local externa'
	
	def funcion_anidada():
		variable_anidada = 'Variable local anidada'
		# Trabajamos con la variable externa sin hacerla local:
		nonlocal variable_local_externa
		print(variable_local_externa)
		variable_local_externa = 'Nuevo valor variable local externa'
		print(variable_local_externa)
	
	funcion_anidada()

funcion_externa()
```

Si solo necestiasemos acceder a `variable_local_externa` no seria necesario hacer uso  de `nonlocal`, sin embargo, como la consultaremos y modificaremos, debemos hacer lo equivalente a global, pero explicitamente le estamos diciendo que nos referimos a la variable de funcion externa. Por ende, `global` y `nonlocal` tienen el mismo principio pero una es para variables de bloques de codigo, la otra para todo el programa.

