#Python #DiseñoClases

La actividad propone hacer una clase llamada `Orden`, la cual tiene metodo `__str__` y atributos: `+contador_ordenes: int <<class variable>>`, `-id_oden: int` y `-productos: <<producto list>>`. Tambien una clase `Producto` que cuenta con el metodo `__str__` y los atributos: `contador_productos: int <<class variable>>`, `-id_pruducto: int`, `-nombre: str` y `-precio: float`.


> [!example] Cuando hacemos un diagrama UML, el `-` en una variable significa que el atributo debe estar encapsulado y  el `+` significa que no debe de estar encapsulado.


```python
class Producto:
	id_producto = 0
	def __init__(self, nombre, precio):
		self.__id_producto = Producto.__aumentarID()
		self.__nombre = nombre
		self.__precio = precio

	@classmethod
	def __aumentarID(cls):
		cls.id_producto += 1
		return cls.id_producto

	@property
	def precio(self):
		return self.__precio

	def __str__(self):
		return f'{self.__id_producto:^3}: {self.__nombre:<20} | ${self.__precio:>11} MXN'

class Orden:
	contador_ordenes = 0
	def __init__(self, *productos):
		self.__productos = list(productos)
		self.__id_orden = Orden.__aumentarID()
		
	@classmethod
	def __aumentarID(cls):
		cls.contador_ordenes += 1
		return cls.contador_ordenes

	def addProduct(self, product):
		self.__productos.append(product)
	
	def calcTotal(self):
		total = 0
		for producto in self.__productos:
			total += producto.precio
		return str(total)
		
	def __str__(self):
		productos_str = ''
		print(''.center(45,'-'))
		for producto in self.__productos:
			productos_str += producto.__str__() + '\n'
		return f'Orden {self.__id_orden}: \n{productos_str}{'':>5}{'Total':<20} | ${Orden.calcTotal(self):>11} MXN'

producto1 = Producto('Camiseta', 250.00)
producto2 = Producto('Pantalon', 400000.00)
orden1 = Orden(producto1, producto2)
producto3 = Producto('Camisa', 200)
producto4 = Producto('Playera', 135.50)
orden1.addProduct(producto4)
print(orden1)
orden2 = Orden(producto2, producto3, producto1, producto4)
print(orden2)

```


> [!success] Acceder a una Parte del Objeto Ya Creado
> Para acceder a una variable o una función de un objeto ya creado, debemos nombrar a la clase en minúscula la primer letra, de esta forma estamos accediendo al objeto, por ejemplo `producto`, seguido del `.` y el atributo o función a la que se quiera acceder.
