#Python #Clases #ClasesAbstractas

La clase abstracta hace que al heredar un metodo, cambie su comportamiento dependiendo de el tipo de clase hija. Un ejemplo es el de las figuras geométricas, en las cuales para calcular el area es necesario saber las características de la figura, sin embargo se puede crear un método de clase abstracto.

Cuando agregamos un método abstracto a la clase padre, ahora es obligatorio que la clase hija tenga una implementación de ese método.

Cuando creamos una clase con un metodo abstracto, ahora toda la clase se vuelve abstracta. Eso significa que no podemos crear objetos o instancias de una clase abstracta, solo sirve para hacer clases heredadas.

> [!example] La libreria de la clase abstracta es `abc = Abstract Base Class`

>Clase Abstracta: FiguraGeometrica

```python
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
	def __init__(self, xxxxx):
		pass

	@abstractmethod
	def calcularArea(self):
		pass
```

Ahora cuando creemos una clase hija de `FiguraGeometrica`, debemos agregar el metodo `calcularArea` para que pueda ser valida la clase, de lo contrario regresara un error.

### Nuevo MRO

Cuando hagamos uso de las clases abstractas en python, ahora, el orden cambiara a `ABC` y posteriormente a `Object`.

```python
print(FiguraGeometrica.mro())
```