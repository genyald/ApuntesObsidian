Para nuestras instancias ya creadas, podemos acceder directamente a los atributos o modificarlos (se les conoce como atributos publicos), lo cual podria causar un comportamiento no deseado si se llega a cambiar algo que no deberia. Para eso existe el concepto de encapsulamiento que es, basicamente, limitar la modificación de esos valores. 

## Encapsulamiento Sugestivo

Para restringir el acceso a valores de nuestra instancia basta solamente con agregar un guion bajo o un doble guion bajo `_` / `__`:

```python
class Persona:
	def __init__(self, nombre, apellidos, edad):
		self._nombre = nombre   # Solo es valido usar _ al crear una clase
```

Ahora nombre es un atributo encapsulado, por lo cual no es correcto acceder a este valor o modificarlo **fuera de la clase**. En teoría aun se puede pero no es una buena practica.

>Para limitarlo realmente, con doble guion bajo, ya no podremos acceder directamente a estos parametros, por lo que es mas funcional `__`.

> [!warning] Modificadores de acceso
> A diferencia de otros lenguajes de programacion, python no cuenta con modificadores de acceso, por eso mismo se hace uso de la practica de los guiones bajos por convencion. Si ves un guion bajo en una variable, esta no se debe modificar directamente fuera de la clase que lo genera.

## Metodo Set y Metodo Get

Hay una forma de limitar realmente el acceso a los atributos de nuestras clases y es mediante el método set y get.

>Esto se puede hacer con todos los parametros de nuestra clase.

| get | obtener/recuperar |
| :-: | :---------------- |
| set | colocar/modificar |


### Método Get

```python
class Persona:
	def __init__(self, nombre, apellido, edad):
		self._nombre = nombre
		self._apellido = apellido
		self._edad = edad
		
	def nombre(self):    # Comienza el metodo set
		return self._nombre

persona1 = Persona('Juan', 'Perez', 22)
print(persona1.nombre())
```

Para asegurarnos que nuestro parametro no sea accedido, se hace uso de [[Decoradores]], específicamente el decorador `@property`:

```python
class Persona:
	def __init__(self, nombre, apellido, edad):
		self._nombre = nombre
		self.apellido = apellido
		self.edad = edad
		
	@property
	def nombre(self):
		return self._nombre

persona1 = Persona('Juan', 'Perez', 22)
print(persona1.nombre)
```

Ahora, gracias a método `property`, no necesitamos mandar a llamar a la función nombre con parentesis `()`, si no que se manda a llamar como un parámetro, el cual no se esta accediendo directamente de la clase, si no que la función nombre no hace el get.

### Método Set

Para hacer uso del metodo get, necesitamos el uso de uno de los [[Decoradores]], el cual es `@nombre.setter`, el parámetro es la parte `nombre`, asi como en la función decorada de nombre para recuperar el parametro, es nombre el que hara uso de ____nombre.

```python
class Persona:
	def __init__(self, nombre, apellido, edad):
		self._nombre = nombre
		self.apellido = apellido
		self.edad = edad
		
	@property
	def nombre(self):
		return self._nombre
		
	@nombre.setter
	def nombre(self, nombre):
		self._nombre = nombre

persona1 = Persona('Juan', 'Perez', 22)
print(persona1.nombre)
persona1.nombre = 'Pedro Pedro Pedro'
print(persona1.nombre)
```

El decorador acaba de hacer que la función nombre se pueda acceder como un dato que se puede modificar, sin necesidad de llamar la función de la instancia creada. 

> [!info] Getter para Setter
> Para poder hacer el método set, necesitamos haber hecho uso del decorador `@property` y posteriormente usamos `@nombre.setter`, de lo contrario obtendremos un error.
