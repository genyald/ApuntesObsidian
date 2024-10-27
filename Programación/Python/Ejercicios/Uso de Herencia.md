#Python #Ejercicio #Herencia 

> [!example] EJERCICIO
> Definir una clase padre llamada `Vehiculo` y dos clases hijas llamadas `Coche` y `Bicicleta`, las cuales heredan de la clase padre `Vehiculo`.
>
La clase padre debe tener los siguientes atributos y metodos:
>
> 	Vehiculo (Clase Padre):
> 	- Atributos: Color, Ruedas
> 	- Metodos: __init__() y __str__
> 
> Las clases hijas deben tener lo siguientes métodos y atributos:
> 1era Clase:
> 
> 	Coche (Clase Hija del Vehículo):
> 	- Atributos: Velocidad (km/h)
> 	- Metodos: __init__() y __str__()
> 2da Clase
> 
>	Bicicleta (Clase Hija del Vehiculo):
>	- Atributos: Tipo (montaña, urbana, carreras, etc)
>	- Metodos: __init__() y __str__()

```python
class Vehiculo:
	def __init__(self, color, ruedas):
		self._color = color
		self._ruedas = ruedas
		
	def __str__(self):
		return f'El Vehiculo {self._color}, con {self._ruedas} ruedas'

class Coche(Vehiculo):
	def __init__(self, color, ruedas, velocidad):
		super().__init__(color, ruedas)
		self._velocidad = velocidad

	def __str__(self):
		return f'{super().__str__()} es un Coche y tiene una velocidad de {self._velocidad} km/h'

class Bicicleta(Vehiculo):
	def __init__(self, color, ruedas, tipo):
		super().__init__(color, ruedas)
		self._tipo = tipo

	def __str__(self):
		return f'{super().__str__()} es una Bicicleta tipo {self._tipo}'

coche1 = Coche('Rojo', 4, 250)
bicicleta1 = Bicicleta('Verde', 2, 'Montaña')

print(coche1)
print(bicicleta1)
```
