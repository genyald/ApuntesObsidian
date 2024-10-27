#Python #MicroPython

Machine es la libreria por defecto en micropython que se encarga de controlar el dispositivo fisico mediante la sintaxis de python.

Advertencia
Machine te deja modificar directamente los elementos del dispositivo, por lo que el uso indebido de este puede provocar congelacion de la placa, crasheos y en el peor de los casos, el da;o directo del dispositivo.

# Acceso a la memoria

El modulo memoria permite acceder a cuatro objetos diferentes que modifican en crudo la memoria:

```python
machine.mem8             [[Lee]] o escribe 8 bits de la memoria
```

```python
machine.mem16             [[Lee]] o escribe 16 bits de la memoria
```

```python
machine.mem32             [[Lee]] o escribe 32 bits de la memoria
```

Ejemplo de codigo usando el acceso a la memoria:

```python
import machine
from micropython import const

GPIOA = const(0x48000000)
GPIO_BSRR = const(0x18)
GPIO_IDR = const(0x10)

# set PA2 high
machine.mem32[GPIOA + GPIO_BSRR] = 1 << 2

# read PA3
value = (machine.mem32[GPIOA + GPIO_IDR] >> 3) & 1
```