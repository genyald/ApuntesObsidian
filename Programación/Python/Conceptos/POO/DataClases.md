#Python #DataClases  #Decoradores #Clases 

`dataclases` es un modulo de python que provee decoradores y funciones que de manera automatica se agregan a nuestras clases y tambien generan de forma automatica metodos como `__init__` o `__repr__` lo cual agrega funcionalidad de manera automatica a nuestras clases.

```python
from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Persona:
	nombre: str
	apellido : str
	contador_personas : ClassVar[int] = 0

persona1 = Persona('Juan', 'Perez')
print(f'{persona1!r}')
print(Persona.contador_personas)

# Variables de instancia
print('Variables de instancia', persona1.__dict__)
```

Como se puede apreciar, vuelve muy facil el crear una clase sencilla y le da formato al metodo `__repr__`, lo cual puede optimizar bastante el proceso de escribir codigo de clases sencillas. Ademas, contamos con el metodo `__post_init__`, el cual se ejecuta despues de init y nos permite agregarle funcionalidades a este:

```python
from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Persona:
	nombre: str
	apellido : str
	contador_personas : ClassVar[int] = 0
	
	def __post_init__(self):
		if not self.nombre or not self.apellido:
			raise ValueError('No se permiten valores vacios')

persona1 = Persona('', '')
```

Tambien podemos comprar la igualdad de dos clases creadas con dataclases, por lo que implementa el metodo `__eq__` (equal) de manera automatica.

Para comprobar igualdad entre objetos:

```python
from dataclasses import dataclass

@dataclass
class Persona:
	nombre: str
	apellido : str

persona1 = Persona('Juan', 'Perez')
persona2 = Persona('Juan', 'Perez')

print('Objetos Iguales?', persona1 == persona2)
```

Podemos activar la implementacion del metodo al declarar el decorador del dataclas:

- `@dataclass(eq=True)` por defecto `True`
- `@dataclass(frozen=True)` por defecto `False`, hace que la clase sea inmutalbe, con esto podemos meter el objeto en un [[Set]].

Para hacer una clase que contiene otra declaracion de clase en otra de estas, podemos hacer que uno de los nombres de las variables contenga el nombre de la otra clase:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Domicilio:
    calle: str
    numero: int = 0

@dataclass(frozen=True)
class Persona:
    nombre: str
    apellido: str
    domicilio: Domicilio

domicilio1 = Domicilio('Saturno', 32)
persona1 = Persona('Pedro', 'Jimenez', domicilio1)
persona2 = Persona('Juan', 'Perez', domicilio=('Marte', 12))
sets = {persona1, persona2}

print(sets)
```

Lo mejor y mas recomendable es que si se va a modificar demasiado el comportamiento de la clase o se cambia su comportamiento natual en gran medida, usemos el metodo convencional que conocemos.

