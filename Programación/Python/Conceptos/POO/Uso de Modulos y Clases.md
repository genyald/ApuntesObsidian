#Python #Modulos #Clases

Podemos importar otros archivos a nuestros programas en python, de tal manera que podemos traer clases para posteriormente usarlas y hacer un codigo mas complejo en varios archivos manteniendo un orden. Para ello hacemos uso de el comando `from (...) import (...) as (...)` (el as no es necesario).

```python
from code_py.Persona import Persona
# from code_py.Persona import *
```

Ahora podemos hacer uso de la clase `Persona` en el archivo `Persona` en la carpeta `code_py` con todos sus parámetros y metodos:

```python
persona1 = Persona('Juan', 'Perez', 22)
persona1.imprimir()
```


> [!important] Todo el código del archivo que este fuera de la clase se ejecutará


> [!question] ¿Podemos preguntar que archivo es la parte de codigo que estamos ejecutando?
> Si, podemos hacer uso de `__name__`, este nos responderá con la parte actual que estamos ejecutando el codigo, por ejemplo:
> ```python
> print(__name__)
>```

## Limitar la Ejecucion del Codigo Cuando se Usa un Archivo Como Modulo

Para limitar la parte del codigo que estamos limitando, podemos hacer uso de `__name__` como conficion:

```python
if __name__ == '__main__':
	print('Este codigo se esta ejecutando porque no es un modulo importado')
```