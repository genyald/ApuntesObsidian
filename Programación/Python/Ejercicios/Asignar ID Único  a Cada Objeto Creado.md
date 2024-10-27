En el siguiente codigo, podemos apreciar que se crea una clase, esta cuenta con una variable de clase que sera aumentada cuando se use el metodo `__init__`, el cual inicializa una instancia, podiendo saber el numero de objeto creado (`id`).

```python
class Persona:
	id = 0
	def __init__(self, nombre, edad):
		self._idObject = Persona.__plusId()
		self._nombre = nombre
		self._edad = edad
		
	@classmethod
	def __plusId(cls):
		cls.id += 1
		return cls.id
		
	def __str__(self):
		return f'ID Object: {self._idObject}, {self._nombre}, {self._edad}'

object1 = Persona('Juan', 22)
print(object1)
object2 = Persona('Pedro', 25)
print(object2)
object3 = Persona('Juan', 27)
print(object3)
```

Le ponemos dunder a `plusId` para volverlo un método privado y de esta manera no pueda ser accedido fuera de la clase.

> [!summary] Debe ser un `classmethod` debido a que este es inicializado antes que la instancia, por lo que no se puede mandar a llamar un metodo de instancia al momento de inicializarla.

