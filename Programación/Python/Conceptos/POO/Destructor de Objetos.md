#Python #Object #Destructor

El método destructor de objetos es una herramienta para liberar espacio en la memoria ram en un momento dado del programa. No se debe confundir con el recolector de basura en python. El recolector de basura destruye los objetos que no estén siendo apuntados por alguna literal o variable.

>En la clase `Persona` ya tenemos definido el metodo `__del__`, el cual agregara un comportamiento a la instancia cuando esta misma sea borrada.

```python
from code_py.Persona import Persona

print('Creacion de Objetos'.center(50, '-'))
persona1 = Persona('Brandon', 'Rodriguez', 18)
persona1.imprimir()

print('Destruccion de Objetos'.center(50, '-'))
del persona1
```

