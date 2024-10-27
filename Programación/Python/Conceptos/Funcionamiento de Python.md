#Python

Python es un lenguaje de programación creado por Guido Van Rossum en la década de 1980, en los Países Bajos, se caracteriza por una sintaxis clara y legible, lo cual facilita la comprensión y lectura del código. 

Python es **interpretado**, lo que significa que no es como C o Java, que se convierte a un lenguaje de máquina, sino que se ejecuta en una máquina virtual (Python Virtual Machine - PVM).

## Características clave de python

- Sintaxis simple
- [[Multiparadigma]]
- Su biblioteca base es muy amplia
- Portabilidad
- Gran comunidad

> [!INFO] Versión más usada
> La versión mas utilizada actualmente es la 3.x

## Funcionamiento

>- Compilación a bytecode
	- EL código fuente se compila a bytecode (instrucciones intermedias independientes de la plataforma), se maneja en archivos .pyc

>- Ejecucion en la PVM
	- La Python Virtual Machine interpreta y ejecuta el bytecode
	- Administra la memoria, objetos y operaciones de bajo nivel

>- JIT (Just-In-Time)
	- Algunas implementaciones de Python (como CPython) usan tecnicas de implementación JIT para aumentar el rendimiento.

### ¿Qué es el bytecode?

- Es una representación intermedia en el codigo de Python.
- Cuando se escribe un programa, el **compilador** de PVM traduce tu codigo fuente a instrucciones bytecode.
	- Estas instrucciones son independientes de la plataforma y se alamacenan en archivos .pyc

#### ¿Por qué se utiliza?

Permite que el bytecode sea portable e independiente de la plataforma.

#### Ejemplo:

```python
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Juan")
```

El compilador generaría un bytecode similar a este:

```
LOAD_CONST 0
LOAD_FAST 0
FORMAT_VALUE 0
CALL_FUNCTION 1
POP_TOP
LOAD_CONST 1
RETURN_VALUE
```


> [!success] Ventajas
> Es más eficiente que el código fuente en terminos de ejecución, digamos que se convierte en instrucciones más optimas, además permite una distribución segura del código sin revelar el código fuente.
