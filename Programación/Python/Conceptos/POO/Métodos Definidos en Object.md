#Python #Object
## `__str__`

El metodo str es un metodo dunder presente en la clase padre, el cual se puede sobrescribir para cambiar el comportamiento de nuestra instancia cuando se mande a imprimir.

```python
# Aqui definimos nuestra clase llamada Persona
class Persona:
	def __init__(self, nombre, apellido, edad):
		self._nombre = nombre
		self._apellido = apellido
		self._edad = edad
		
	def __str__(self):
		return f'Persona[Nombre: {self._nombre}, Apellido: {self._apellido}, Edad: {self._edad}]'

class Empleado(Persona):
	def __init__(self, nombre, apellido, edad, sueldo):
		super().__init__(nombre, apellido, edad)
		self._sueldo = sueldo

persona1 = Persona('Juan Carlos', 'Castro', 22)
empleado1 = Empleado('Carballo', 'Pichardo', 22, 12000)
print(persona1)
print(empleado1)
```

Para este caso especifico, normalmente cuando mandamos a imprimir el objeto persona1, por defecto, la clase `__str__` nos devuelve la direccion de memoria donde se encuentra este, sin embargo, ahora que remplazamos este método, cuando sea mandado a llamar a imprimir o como un string, este nos devolverá los datos del objeto tal cual lo programamos.

> [!info] Sobreescritura de metodos
> Cuando tenemos un método en una clase padre y lo volvemos a usar para definirlo en una clase hija, el método será sobrescrito en automático.