#Python #Ejercicio #Global #Vars 

El siguiente ejercicio es para entender a fondo como funcionan las variables globales y las locales en python:

```python
# Definimos una variable global
contador = 0

def mostrar_contador():
	print(contador)

def modificar_contador(c):
	contador = c

modificar_contador(5)
mostrar_contador()
```

Como se puede observar, al intentar modificar la variable contador en esa misma funcion, la variable se considera como local, osea que fue declarada ahi, para evitar eso debemos hacer uso de la paralabra `global`:

```python
# Definimos una variable global
contador = 0

def mostrar_contador():
	print(contador)

def modificar_contador(c):
	global contador
	contador = c

mostrar_contador()
modificar_contador(5)
mostrar_contador()
```